from ReadCSV import ReadCSV
from MainModel import MainModel
from Checker import Checker
from Logger import Logger

class Manager:

    def __init__(self, url):
        self.CsvFile = ReadCSV('../Data/phishing.csv').GetCSV()
        self.Logger = Logger('../Data/Logs.txt')
        self.URL = url
        self.Logger.Log(f'Request With URL Data - {url}')

    def TrainTheModel(self):
        self.MainModel = MainModel(self.CsvFile)
        self.MainModel.DoAllTheSession()
        self.Logger.Log('Done Training The Model')

    def load_from_url(self):
        self.Checker = Checker(self.MainModel, self.URL)
        self.Checker.Checks()
        self.Logger.Log('Process The URL Data')
        return self.Checker.CheckUrlRow()

    def run(self):
        self.TrainTheModel()
        return self.load_from_url()

