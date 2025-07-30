from Loader import Loader
from Cleaner import Cleaner
from Trainer import Trainer
from Tester import Tester
from Classifier import Classifier
from Logger import Logger

class Manager:

    def __init__(self):
        self.Logger = Logger('Data/Logs.txt')
        self.Loader = None
        self.DataFrame = None
        self.Cleaner = None
        self.Trainer = None
        self.Model = None
        self.Tester = None
        self.Classifier = None

    def load_file(self):
        self.Loader = Loader()
        self.Loader.load_from_path('Data/phishing.csv')
        self.DataFrame = self.Loader.get_the_dataframe()

    def clean_the_file(self):
        self.Cleaner = Cleaner()
        self.Cleaner.load_dataframe(self.DataFrame)
        self.Cleaner.set_index()
        self.Cleaner.drop_null()
        self.Cleaner.drop_duplicates()
        self.Cleaner.reset_index()
        self.DataFrame = self.Cleaner.get_dataframe()

    def train_the_model(self):
        self.Trainer = Trainer()
        self.Trainer.load_dataframe(self.DataFrame)
        self.Trainer.load_uniques_to_all_precent()
        self.Trainer.load_numbers_to_all_precents()
        self.Trainer.clean_zeroes()
        self.Trainer.calculate_the_precents()
        self.Model = self.Trainer.get_the_model()
        self.Logger.log('Done Training The Model')

    def test_the_model(self):
        self.Tester = Tester(self.DataFrame, self.Trainer)
        accurate_of_the_model = self.Tester.test()
        self.Logger.log(f'How The ModelString Is - {accurate_of_the_model}')

    def load_from_url(self, url):
        self.Classifier = Classifier(self.Trainer, url)
        self.Logger.log(f'Request With URL Data - {url}')
        self.Classifier.check_the_types_of_url_items()
        return self.Classifier.run_no_the_url()

    def run(self):
        self.load_file()
        self.clean_the_file()
        self.train_the_model()
        self.test_the_model()

