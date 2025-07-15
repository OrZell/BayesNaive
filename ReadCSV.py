import pandas as pd

class ReadCSV:

    def __init__(self, path):
        self.CSV = pd.read_csv(path, index_col='Index').dropna().drop_duplicates().reset_index(drop=True)

    def GetCSV(self):
        return self.CSV