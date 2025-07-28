import pandas as pd

class Trainer:

    def __init__(self, dataframe:pd.DataFrame):
        self.DataFrame = dataframe[dataframe.index < 0.7 * dataframe.shape[0]]
        self.ExempleRow = dataframe.iloc[0].tolist()
        self.LenOfPrimaryTable = dataframe.shape[0]
        self.TargetColumn = dataframe.columns.tolist()[-1]
        self.UniquesInTargetColumn = dataframe[self.TargetColumn].unique().tolist()
        self.AllRelevantColumns = dataframe.columns.tolist()[:-1]
        self.AllPrecents = {}
        self.AllTables = {}
        self.AllTablesLen = {}
        self.IsThereZeroes = False

    def load_uniques_to_all_precent(self):
        for unique in self.UniquesInTargetColumn:
            self.AllPrecents[unique] = {}
            self.AllTables[unique] = self.DataFrame[self.DataFrame[self.TargetColumn] == unique]
            self.AllTablesLen[unique] = self.AllTables[unique].shape[0]

    def load_numbers_to_all_precents(self):
        for uniquePrime in self.UniquesInTargetColumn:
            for col in self.AllRelevantColumns:
                self.AllPrecents[uniquePrime][col] = [{}]
                uniques = self.DataFrame[col].unique().tolist()
                for unique in uniques:
                    list_count = self.DataFrame[self.DataFrame[self.TargetColumn] == uniquePrime][col].tolist()
                    counts = list_count.count(unique)
                    if counts == 0:
                        self.IsThereZeroes = True
                    self.AllPrecents[uniquePrime][col][0][unique] = counts
                self.AllPrecents[uniquePrime][col].append(self.AllTablesLen[uniquePrime])

    def clean_zeroes(self):
        if self.IsThereZeroes:
            for Target in self.AllPrecents:
                for Column in self.AllPrecents[Target]:
                    if 0 in self.AllPrecents[Target][Column][0].values():
                        for Unique in self.AllPrecents[Target][Column][0]:
                            self.AllPrecents[Target][Column][0][Unique] += 1
                        self.AllPrecents[Target][Column][1] += 1
            self.IsThereZeroes = False

    # def LoadNumbersToAllPrecents(self):
    #     for uniquePrime in self.UniquesInTargetColumn:
    #         for col in self.AllRelevantColumns:
    #             self.AllPrecents[uniquePrime][col] = [{}]
    #             uniques = self.PrimaryDF[col].unique().tolist()
    #             for unique in uniques:
    #                 listCount = self.PrimaryDF[self.PrimaryDF[self.TargetColumn] == uniquePrime][col].tolist()
    #                 counts = listCount.count(unique)
    #                 if counts == 0:
    #                     self.IsThereZeroes = True
    #                 self.AllPrecents[uniquePrime][col][0][unique] = counts
    #             self.AllPrecents[uniquePrime][col].append(self.AllTablesLen[uniquePrime])

    def calculate_the_precents(self):
        for Target in self.AllPrecents:
            for Column in self.AllPrecents[Target]:
                for Unique in self.AllPrecents[Target][Column][0]:
                    precents = self.AllPrecents[Target][Column][0][Unique] / self.AllPrecents[Target][Column][1]
                    self.AllPrecents[Target][Column][0][Unique] = float(precents)

    def load_clean_calculate(self):
        self.load_uniques_to_all_precent()
        self.load_numbers_to_all_precents()
        self.clean_zeroes()
        self.calculate_the_precents()

    def get_the_model(self):
        return self.AllPrecents