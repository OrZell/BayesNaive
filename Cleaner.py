import pandas as pd

class Cleaner:

    def __init__(self):
        self.File = None

    def load_file(self, dataframe:pd.DataFrame):
        self.File = dataframe

    def set_index_column(self):
        self.File.set_index('Index', inplace=True)

    def drop_nans(self):
        self.File.dropna(inplace=True)

    def drop_duplicates(self):
        self.File.drop_duplicates(inplace=True)

    def reset_index(self):
        self.File.reset_index(drop=True, inplace=True)

    def get_the_dataframe(self):
        return self.File