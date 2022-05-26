import lightning as L

from hackernews_app.flows.model_serve import ModelServeFlow
import time

class HackerNewsDataProcesses(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.model_service = ModelServeFlow()

    def run(self):
        self.model_service.run()

        while self.model_service.server_one is False:
            time.sleep(5)

    def configure_layout(self):
        return {"name": "Home", "content": self.model_service}


if __name__ == "__main__":
    app = L.LightningApp(HackerNewsDataProcesses())
