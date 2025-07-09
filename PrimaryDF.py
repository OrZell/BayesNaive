import pandas as pd

class PrimaryDF:

    def __init__(self, MainTable:pd.DataFrame):
        self.PrimaryTable = MainTable

    @property
    def CleanTheTable(self):
        self.PrimaryTable = self.PrimaryTable.dropna()

    @property
    def LenOfPrimaryTable(self):
        return self.PrimaryTable.shape[0]

    @property
    def TargetColumn(self):
        return self.PrimaryTable.columns.tolist()[-1]

    @property
    def UniquesInTargetColumn(self):
        return self.PrimaryTable[self.TargetColumn].unique().tolist()

    @property
    def AllRelevanteColumns(self):
        return self.PrimaryTable.columns.tolist()[1:-1]

