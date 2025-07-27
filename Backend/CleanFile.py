import pandas as pd


class CleanFile:

    def __init__(self, df:pd.DataFrame):
        self.CSVFile = df

    def SetIndex(self):
        self.CSVFile.set_index('Index', inplace=True)

    def DropNull(self):
        self.CSVFile.dropna(inplace=True)

    def DropDuplicates(self):
        self.CSVFile.drop_duplicates(inplace=True)

    def ResetIndex(self):
        self.CSVFile.reset_index(inplace=True, drop=True)

    def GetFile(self):
        return self.CSVFile