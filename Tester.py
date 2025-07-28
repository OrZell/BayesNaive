import pandas as pd
from Trainer import Trainer


class Tester:

    def __init__(self, dataframe:pd.DataFrame, trainer:Trainer):
        self.DataFrame = dataframe[dataframe.index >= 0.7 * dataframe.shape[0]]
        self.Trainer = trainer
        self.AllPrecents = self.Trainer.get_the_model()
        self.AllColumns = self.Trainer.AllRelevantColumns
        self.AllTablesLen = self.Trainer.AllTablesLen
        self.LenOfPrimaryTable = self.Trainer.LenOfPrimaryTable

    def test(self):
        total = []
        for i in range(self.DataFrame.shape[0]):
            row = self.DataFrame.iloc[i].tolist()
            answer = row[-1]
            row = row[:-1]
            total.append(self.check_test_row(row, answer))
        return total.count(True) / len(total)


    def check_test_row(self, row, answer):

        answers = {}

        for Unique in self.AllPrecents:
            num = 1
            for i in range(len(row)):
                num = num * self.AllPrecents[Unique][self.AllColumns[i]][0][row[i]]
            num = num * self.AllTablesLen[Unique] / self.LenOfPrimaryTable
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1] == answer