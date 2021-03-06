import os


class TopicClassificationDataConfig:
    """Configuration for topic classification data."""

    classes = [
        "Education",
        "Business",
        "Sports",
        "Technology",
        "News and Politics",
        "Lifestyle",
        "Culture and Arts",
        "Entertainment",
    ]

    main_categories = {
        "Education": ["EDUCATION", "COLLEGE"],
        "Business": ["BUSINESS", "MONEY"],
        "Sports": ["SPORTS"],
        "Technology": ["TECH", "SCIENCE"],
        "News and Politics": [
            "POLITICS",
            "BLACK VOICES",
            "QUEER VOICES",
            "LATINO VOICES",
            "WOMEN",
            "IMPACT",
            "RELIGION",
            "CRIME",
            "GOOD NEWS",
            "MEDIA",
            "WEIRD NEWS",
            "WORLD NEWS",
            "THE WORLDPOST",
            "WORLDPOST",
        ],
        "Lifestyle": [
            "WELLNESS",
            "TRAVEL",
            "STYLE & BEAUTY",
            "PARENTING",
            "HEALTHY LIVING",
            "FOOD & DRINK",
            "HOME & LIVING",
            "ENVIRONMENT",
            "PARENTS",
            "STYLE",
            "TASTE",
            "GREEN",
            "FIFTY",
        ],
        "Culture and Arts": ["ARTS & CULTURE", "CULTURE & ARTS", "WEDDINGS", "DIVORCE", "ARTS"],
        "Entertainment": ["ENTERTAINMENT", "COMEDY"],
    }


class TopicClassificationModelConfig:
    model_name = "distilbert-base-uncased"
    max_epochs = 5


class TopicClassificationConfig(TopicClassificationModelConfig, TopicClassificationDataConfig):
    pass


class BaseDataConfig:
    least_fav_topic_count = 4
    val_split_pct = 0.2


class BaseConfig:
    """General configuratios."""

    num_epochs = 2
    num_batches_show_loss = 100  # Number of batchs to show loss
    # Number of batchs to check metrics on validation dataset
    num_batches_validate = 1000
    batch_size = 128
    learning_rate = 0.0001
    num_workers = os.cpu_count()  # Number of workers for data loading
    num_clicked_news_a_user = 50  # Number of sampled click history for each user
    num_words_title = 20
    num_words_abstract = 50
    word_freq_threshold = 1
    entity_freq_threshold = 2
    entity_confidence_threshold = 0.5
    negative_sampling_ratio = 2  # K
    dropout_probability = 0.2
    # Modify the following by the output of `src/dataprocess.py`
    word_embedding_dim = 300
    # Modify the following only if you use another dataset
    entity_embedding_dim = 100
    # For additive attention
    query_vector_dim = 200


class TANRConfig(BaseConfig, BaseDataConfig, TopicClassificationConfig):
    # For CNN
    num_filters = 300
    window_size = 3
