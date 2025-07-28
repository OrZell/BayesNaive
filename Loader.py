import pandas as pd

class Loader:

    def __init__(self):
        self.File = None

    def LoadFromPath(self, path):
        try:
            self.File = pd.read_csv(path)
        except:
            raise 'No Such File'

    def GetTheFile(self):
        if self.File is None:
            raise 'File Not Loaded'
        return self.File