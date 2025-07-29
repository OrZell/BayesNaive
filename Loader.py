import pandas as pd

class Loader:

    def __init__(self):
        self.File = None

    def load_from_path(self, path:str):
        try:
            self.File = pd.read_csv(path)
        except:
            raise 'No Such File'

    def get_the_file(self):
        if self.File is None:
            raise 'File Not Loaded'
        return self.File