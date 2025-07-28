from Trainer import Trainer
from Loader import Loader
from Tester import Tester

class BackManager:

    def __init__(self):
        self.Loader = Loader()
        self.DataFrame = None
        self.Trainer = None
        self.Tester = None

    def load_file(self):
        self.Loader.load_from_path(f'phishing.csv')
        self.DataFrame = self.Loader.get_the_file()

    def training_model(self):
        self.Trainer = Trainer(self.DataFrame)
        self.Trainer.load_clean_calculate()

    def test_the_model(self):
        self.Tester = Tester(self.DataFrame, self.Trainer)

    def load_train_test(self):
        self.load_file()
        self.training_model()
        self.test_the_model()

    def get_the_model(self):
        return self.Trainer.get_the_model()
