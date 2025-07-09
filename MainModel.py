from PrimaryDF import PrimaryDF
import pandas as pd

class MainModel:

    def __init__(self, MainDF:PrimaryDF):
        self.PrimaryDF = MainDF.GetTheDF
        self.LenOfPrimaryTable = MainDF.LenOfPrimaryTable
        self.TargetColumn = MainDF.TargetColumn
        self.UniquesInTargetColumn = MainDF.UniquesInTargetColumn
        self.AllRelevantColumns = MainDF.AllRelevantColumns
        self.AllPrecents = {}
        self.AllTables = {}
        self.AllTablesLen = {}
        self.IsThereZeroes = False

    @property
    def LoadUniquesToAllPrecent(self):
        for unique in self.UniquesInTargetColumn:
            self.AllPrecents[unique] = {}
            self.AllTables[unique] = self.PrimaryDF[self.PrimaryDF[self.TargetColumn] == unique]
            self.AllTablesLen[unique] = self.AllTables[unique].shape[0]

    @property
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

    @property
    def CleanZeroes(self):
        if self.IsThereZeroes:
            for Target in self.AllPrecents:
                for Column in self.AllPrecents[Target]:
                    if 0 in self.AllPrecents[Target][Column][0].values():
                        for Unique in self.AllPrecents[Target][Column][0]:
                            self.AllPrecents[Target][Column][0][Unique] += 1
                        self.AllPrecents[Target][Column][1] += 1
        self.IsThereZeroes = False

    @property
    def CalculateThePrecents(self):
        for Target in self.AllPrecents:
            for Column in self.AllPrecents[Target]:
                for Unique in self.AllPrecents[Target][Column][0]:
                    precents = self.AllPrecents[Target][Column][0][Unique] / self.AllPrecents[Target][Column][1]
                    self.AllPrecents[Target][Column][0][Unique] = float(precents)

