import pandas as pd

class Loader:

    def __init__(self):
        self.DataFrame = None

    def load_from_path(self, path):
        try:
            self.DataFrame = pd.read_csv(path)
        except:
            raise 'File Not Found'

    def get_the_dataframe(self):
        return self.DataFrame