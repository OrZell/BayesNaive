import pandas as pd

class MainModel:

    def __init__(self, MainDF:pd.DataFrame):
        self.PrimaryDF = MainDF
        self.ExempleRow = MainDF.iloc[0].tolist()
        self.LenOfPrimaryTable = MainDF.shape[0]
        self.TargetColumn = MainDF.columns.tolist()[-1]
        self.UniquesInTargetColumn = MainDF[self.TargetColumn].unique().tolist()
        self.AllRelevantColumns = MainDF.columns.tolist()[:-1]
        self.AllPrecents = {}
        self.AllTables = {}
        self.AllTablesLen = {}
        self.IsThereZeroes = False

    def DoAllTheSession(self):
        self.LoadUniquesToAllPrecent()
        self.LoadNumbersToAllPrecents()
        self.CleanZeroes()
        self.CalculateThePrecents()

    def LoadUniquesToAllPrecent(self):
        for unique in self.UniquesInTargetColumn:
            self.AllPrecents[unique] = {}
            self.AllTables[unique] = self.PrimaryDF[self.PrimaryDF[self.TargetColumn] == unique]
            self.AllTablesLen[unique] = self.AllTables[unique].shape[0]

    def LoadNumbersToAllPrecents(self):
        for uniquePrime in self.UniquesInTargetColumn:
            for col in self.AllRelevantColumns:
                self.AllPrecents[uniquePrime][col] = [{}]
                uniques = self.PrimaryDF[col].unique().tolist()
                for unique in uniques:
                    listCount = self.PrimaryDF[self.PrimaryDF[self.TargetColumn] == uniquePrime][col].tolist()
                    counts = listCount.count(unique)
                    if counts == 0:
                        self.IsThereZeroes = True
                    self.AllPrecents[uniquePrime][col][0][unique] = counts
                self.AllPrecents[uniquePrime][col].append(self.AllTablesLen[uniquePrime])

    def CleanZeroes(self):
        if self.IsThereZeroes:
            for Target in self.AllPrecents:
                for Column in self.AllPrecents[Target]:
                    if 0 in self.AllPrecents[Target][Column][0].values():
                        for Unique in self.AllPrecents[Target][Column][0]:
                            self.AllPrecents[Target][Column][0][Unique] += 1
                        self.AllPrecents[Target][Column][1] += 1
            self.IsThereZeroes = False

    def CalculateThePrecents(self):
        for Target in self.AllPrecents:
            for Column in self.AllPrecents[Target]:
                for Unique in self.AllPrecents[Target][Column][0]:
                    precents = self.AllPrecents[Target][Column][0][Unique] / self.AllPrecents[Target][Column][1]
                    self.AllPrecents[Target][Column][0][Unique] = float(precents)

    def GetTheModel(self):
        return self.AllPrecents