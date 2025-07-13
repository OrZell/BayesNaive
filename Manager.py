from ReadCSV import ReadCSV
from CleanCSV import CleanCSV
from PrimaryDF import PrimaryDF
from MainModel import MainModel
from urlReader import urlReader
from Checker import Checker
from Tester import Tester

class Manager:

    def __init__(self, keys):
        self.ReadCsv = ReadCSV()
        self.Keys = keys

    def run(self):
        self.ReadCSVFile()
        self.TrainTheModel()
        # self.LoadDataToCheck()
        # self.Checking()
        # self.Testing()
        return self.load_from_url()

    def ReadCSVFile(self):
        self.CleanCSV = CleanCSV(self.ReadCsv.ReadFromFile())
        self.PrimaryDF = PrimaryDF(self.CleanCSV.GetTheCSV())

    def TrainTheModel(self):
        self.MainModel = MainModel(self.PrimaryDF)
        self.MainModel.DoAllTheSession()

    # def LoadDataToCheck(self):
    #     self.Checker = Checker(self.MainModel)
    #     choice = input('Want you to load from the current df?')
    #     if choice == 'yes':
    #         self.Checker.ReadFromSameDFWith03(self.PrimaryDF.GetTheDF())
    #     else:
    #         self.Checker.ReadFromNewDF(self.ReadCsv.ReadFromFile())
    #
    # def Checking(self):
    #     self.Answers = self.Checker.CheckEveryRow()
    #
    #
    # def Testing(self):
    #     self.Tester = Tester(self.Answers[0], self.Answers[1])
    #     self.Tester.ComapereTheAnswers()
    #     print(self.Tester.TotalRightPrecents())
    #     return self.Tester.TotalRightPrecents()

    def load_from_url(self):
        self.urlReader = urlReader(self.MainModel)
        return self.urlReader.CheckUrlRow(self.Keys)

