from ReadCSV import ReadCSV
from MainModel import MainModel
from Checker import Checker

class Manager:

    def __init__(self, url):
        self.CsvFile = ReadCSV('../Data/phishing.csv').GetCSV()
        self.URL = url

    def TrainTheModel(self):
        self.MainModel = MainModel(self.CsvFile)
        self.MainModel.DoAllTheSession()

    def load_from_url(self):
        self.Checker = Checker(self.MainModel, self.URL)
        self.Checker.Checks()
        return self.Checker.CheckUrlRow()

    def run(self):
        self.TrainTheModel()
        return self.load_from_url()

