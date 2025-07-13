import pandas as pd

class ReadCSV:

    @staticmethod
    def ReadFromFile():
        # path = input('Enter File Path:')
        path = 'Data/phishing.csv'
        csv = pd.read_csv(path, index_col='Index')
        return csv