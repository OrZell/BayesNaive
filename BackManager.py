from Loader import Loader
from Cleaner import Cleaner
from Trainer import Trainer
from Tester import Tester

class BackManager:

    def __init__(self):
        self.Loader = Loader()
        self.DataFrame = None
        self.Cleaner = None
        self.Trainer = None
        self.Tester = None

    def load_file(self):
        self.Loader.load_from_path('../Data/phishing.csv')
        # self.Loader.load_from_path('Data/phishing.csv')
        self.DataFrame = self.Loader.get_the_file()

    def clean_the_dataframe(self):
        self.Cleaner = Cleaner()
        self.Cleaner.load_file(self.DataFrame)
        self.Cleaner.set_index_column()
        self.Cleaner.drop_nans()
        self.Cleaner.drop_duplicates()
        self.Cleaner.reset_index()
        self.DataFrame = self.Cleaner.get_the_dataframe()

    def training_model(self):
        self.Trainer = Trainer(self.DataFrame)
        self.Trainer.load_clean_calculate()

    def test_the_model(self):
        self.Tester = Tester(self.DataFrame, self.Trainer)

    def load_clean_train_test(self):
        self.load_file()
        self.clean_the_dataframe()
        self.training_model()
        self.test_the_model()

    def get_the_model(self):
        return self.Trainer.get_the_model()
