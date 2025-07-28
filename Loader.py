import pandas as pd

class Loader:

    def __init__(self):
        self.File = None

    def load_file_from_path(self, path):
        try:
            self.File = pd.read_csv(path)
        except:
            raise 'Could Not Load File'

    def get_the_file(self):
        return self.File