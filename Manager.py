from ReadCSV import ReadCSV
from CleanFile import CleanFile
from MainModel import MainModel
from Tester import Tester
from Checker import Checker
from Logger import Logger

class Manager:

    def __init__(self):
        self.CsvFile = ReadCSV('/app/Data/phishing.csv').GetCSV()
        self.Logger = Logger('/app/Data/Logs.txt')

    def CleanTheFile(self):
        self.Cleaner = CleanFile(self.CsvFile)
        self.Cleaner.SetIndex()
        self.Cleaner.DropNull()
        self.Cleaner.DropDuplicates()
        self.Cleaner.ResetIndex()
        self.CsvFile = self.Cleaner.GetFile()

    def TrainTheModel(self):
        self.MainModel = MainModel(self.CsvFile)
        self.MainModel.DoAllTheSession()
        self.Logger.Log('Done Training The Model')

    def TestTheModel(self):
        self.Tester = Tester(self.CsvFile, self.MainModel)
        right = self.Tester.Test()
        self.Logger.Log(f'How Strong The Model Is - {right}')

    def load_from_url(self, url):
        self.Checker = Checker(self.MainModel, url)
        self.Logger.Log(f'Request With URL Data - {url}')
        self.Checker.Checks()
        return self.Checker.CheckUrlRow()

    def run(self):
        self.CleanTheFile()
        self.TrainTheModel()
        self.TestTheModel()

