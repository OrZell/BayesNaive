from MainModel import MainModel
import pandas as pd


class Checker:

    def __init__(self, Model:MainModel):
        # self.CheckedTable = None
        # self.AllColumns = None
        self.Model = Model

    def ReadFromSameDFWith03(self, checkedTable:pd.DataFrame):
        self.CheckedTable = checkedTable[checkedTable.index > 0.7 * len(checkedTable)]
        self.AllColumns = checkedTable.columns.tolist()[:-1]

    def ReadFromNewDF(self, checkedTable:pd.DataFrame):
        self.CheckedTable = checkedTable
        self.AllColumns = checkedTable.columns.tolist()[:-1]

    def CheckEveryRow(self):
        self.Answers = []
        self.ListOfRows = self.CheckedTable.drop(self.CheckedTable.columns[-1], axis=1).values.tolist()
        self.RightAnswers = self.CheckedTable[self.CheckedTable.columns[-1]].tolist()
        AllPrecents = self.Model.GetTheModel()

        for row in self.ListOfRows:
            PrecentsByTragets = {}
            for uniqueTarget in self.Model.UniquesInTargetColumn:
                num = 1
                for i in range(len(row)):
                    num = num * AllPrecents[uniqueTarget][self.AllColumns[i]][0][row[i]]
                num = num * self.Model.AllTablesLen[uniqueTarget] / self.Model.LenOfPrimaryTable
                PrecentsByTragets[uniqueTarget] = num
            sorted_dict = list(dict(sorted(PrecentsByTragets.items(), key=lambda item: item[1])).keys())
            self.Answers.append(sorted_dict[-1])
        return self.RightAnswers, self.Answers