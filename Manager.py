from Loader import Loader
from Cleaner import Cleaner
from Trainer import Trainer
from Tester import Tester
from Classifier import Classifier
from Logger import Logger

class Manager:

    def __init__(self):
        self.Loader = Loader()
        self.Logger = Logger('/app/Data/Logs.txt')
        self.File = None
        self.Cleaner = None
        self.Trainer = None
        self.Tester = None
        self.Classifier = None

    def load_file(self):
        self.Loader.load_file_from_path('/app/Data/phishing.csv')
        self.File = self.Loader.get_the_file()

    def clean_the_file(self):
        self.Cleaner = Cleaner(self.File)
        self.Cleaner.set_index()
        self.Cleaner.drop_null()
        self.Cleaner.drop_duplicates()
        self.Cleaner.reset_index()
        self.File = self.Cleaner.get_the_file()

    def train_the_model(self):
        self.Trainer = Trainer(self.File)
        self.Trainer.do_all_the_session()
        self.Logger.log('Done Training The Model')

    def test_the_model(self):
        self.Tester = Tester(self.File, self.Trainer)
        right = self.Tester.test()
        self.Logger.log(f'How Strong The Model Is - {right}')

    def load_from_url(self, url):
        self.Classifier = Classifier(self.Trainer, url)
        self.Logger.log(f'Request With URL Data - {url}')
        self.Classifier.check_validate_the_url()
        return self.Classifier.check_url_as_row()

    def run(self):
        self.load_file()
        self.clean_the_file()
        self.train_the_model()
        self.test_the_model()

