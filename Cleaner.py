import pandas as pd


class Cleaner:

    def __init__(self, df:pd.DataFrame):
        self.CSVFile = df

    def set_index(self):
        self.CSVFile.set_index('Index', inplace=True)

    def drop_null(self):
        self.CSVFile.dropna(inplace=True)

    def drop_duplicates(self):
        self.CSVFile.drop_duplicates(inplace=True)

    def reset_index(self):
        self.CSVFile.reset_index(inplace=True, drop=True)

    def get_the_file(self):
        return self.CSVFile