import pandas as pd
from Trainer import Trainer


class Tester:

    def __init__(self, MainDF:pd.DataFrame, MainModel:Trainer):
        self.TesterDF = MainDF[MainDF.index >= 0.7*MainDF.shape[0]]
        self.Model = MainModel
        self.AllPrecents = self.Model.get_the_model()
        self.AllColumns = self.Model.AllRelevantColumns
        self.AllTablesLen = self.Model.AllTablesLen
        self.LenOfPrimaryTable = self.Model.LenOfPrimaryTable

    def Test(self):
        total = []
        for i in range(self.TesterDF.shape[0]):
            row = self.TesterDF.iloc[i].tolist()
            answer = row[-1]
            row = row[:-1]
            total.append(self.CheckTestRow(row, answer))
        return total.count(True) / len(total)


    def CheckTestRow(self, row, answer):

        answers = {}

        for Unique in self.AllPrecents:
            num = 1
            for i in range(len(row)):
                num = num * self.AllPrecents[Unique][self.AllColumns[i]][0][row[i]]
            num = num * self.AllTablesLen[Unique] / self.LenOfPrimaryTable
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1] == answer
