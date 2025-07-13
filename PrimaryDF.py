import pandas as pd

class PrimaryDF:

    def __init__(self, MainTable:pd.DataFrame):
        self.PrimaryTable = MainTable

    def LenOfPrimaryTable(self):
        return self.PrimaryTable.shape[0]

    def TargetColumn(self):
        return self.PrimaryTable.columns.tolist()[-1]

    def UniquesInTargetColumn(self):
        return self.PrimaryTable[self.TargetColumn()].unique().tolist()

    def AllRelevantColumns(self):
        return self.PrimaryTable.columns.tolist()[:-1]

    def GetTheDF(self):
        return self.PrimaryTable

