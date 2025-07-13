import pandas as pd

class CleanCSV:

    def __init__(self, csvFile:pd.DataFrame):
        self.CSVFile = csvFile

    def CleanNulls(self):
        self.CSVFile = self.CSVFile.dropna()

    def CleanDuplicates(self):
        self.CSVFile = self.CSVFile.drop_duplicates()

    def ResetIndexes(self):
        self.CSVFile = self.CSVFile.reset_index(drop=True)

    def GetTheCSV(self):
        self.CleanNulls()
        self.CleanDuplicates()
        self.ResetIndexes()
        return self.CSVFile
