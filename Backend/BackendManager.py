from MainModel import MainModel
from ReadCSV import ReadCSV
from Tester import Tester

class BackendManager:

    def __init__(self):
        self.CsvFile = ReadCSV(r'app/Data/phishing.csv').GetCSV()

    def TrainingModel(self):
        self.MainModel = MainModel(self.CsvFile)
        self.MainModel.DoAllTheSession()

    def TestTheModel(self):
        self.Tester = Tester(self.CsvFile, self.MainModel)

    def DoAll(self):
        self.TrainingModel()
        self.TestTheModel()

    def GetTheModel(self):
        return self.MainModel.GetTheModel()
