import torch
import torch.nn as nn
import torch.nn.functional as F

from ml.recsys.models.additive import AdditiveAttention


class NewsEncoder(torch.nn.Module):
    def __init__(self, config, pretrained_word_embedding):
        super().__init__()
        self.config = config
        if pretrained_word_embedding is None:
            self.word_embedding = nn.Embedding(config.num_words, config.word_embedding_dim, padding_idx=0)
        else:
            self.word_embedding = nn.Embedding.from_pretrained(pretrained_word_embedding, freeze=False, padding_idx=0)
        assert config.window_size >= 1 and config.window_size % 2 == 1
        self.title_CNN = nn.Conv2d(
            1,
            config.num_filters,
            (config.window_size, config.word_embedding_dim),
            padding=(int((config.window_size - 1) / 2), 0),
        )
        self.title_attention = AdditiveAttention(config.query_vector_dim, config.num_filters)

    def forward(self, stories):
        """
        Args:
            stories:
                {
                    "title": batch_size * num_words_title
                }
        Returns:
            (shape) batch_size, num_filters
        """
        # batch_size, num_words_title, word_embedding_dim
        title_vector = F.dropout(
            self.word_embedding(stories["title"]),
            p=self.config.dropout_probability,
            training=self.training,
        )
        # batch_size, num_filters, num_words_title
        convoluted_title_vector = self.title_CNN(title_vector.unsqueeze(dim=1)).squeeze(dim=3)
        # batch_size, num_filters, num_words_title
        activated_title_vector = F.dropout(
            F.relu(convoluted_title_vector),
            p=self.config.dropout_probability,
            training=self.training,
        )
        # batch_size, num_filters
        weighted_title_vector = self.title_attention(activated_title_vector.transpose(1, 2))

        return weighted_title_vector
