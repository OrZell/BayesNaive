import pandas as pd

class ReadCSV:

    def __init__(self, path):
        self.CSV = pd.read_csv(path)

    def GetCSV(self):
        return self.CSV