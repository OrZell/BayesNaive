from ReadCSV import ReadCSV
from CleanFile import CleanFile
from MainModel import MainModel
from Tester import Tester

class BackendManager:

    def __init__(self):
        self.CsvFile = ReadCSV(r'/app/Data/phishing.csv').GetCSV()

    def CleanTheFile(self):
        self.Cleaner = CleanFile(self.CsvFile)
        self.Cleaner.SetIndex()
        self.Cleaner.DropNull()
        self.Cleaner.DropDuplicates()
        self.Cleaner.ResetIndex()
        self.CsvFile = self.Cleaner.GetFile()

    def TrainingModel(self):
        self.MainModel = MainModel(self.CsvFile)
        self.MainModel.DoAllTheSession()

    def TestTheModel(self):
        self.Tester = Tester(self.CsvFile, self.MainModel)

    def DoAll(self):
        self.DoAll()
        self.TrainingModel()
        self.TestTheModel()

    def GetTheModel(self):
        return self.MainModel.GetTheModel()
