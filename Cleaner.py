import pandas as pd


class Cleaner:

    def __init__(self):
        self.File = None

    def load_dataframe(self, dataframe:pd.DataFrame):
        self.File = dataframe

    def set_index(self):
        self.File.set_index('Index', inplace=True)

    def drop_null(self):
        self.File.dropna(inplace=True)

    def drop_duplicates(self):
        self.File.drop_duplicates(inplace=True)

    def reset_index(self):
        self.File.reset_index(inplace=True, drop=True)

    def get_the_file(self):
        return self.File