from Frontend.Checker import Checker

class Manager:

    def __init__(self):
        self.j = 'j'

    def checker(self):
        self.Checker = Checker()
        self.Checker.assign()

    def load_from_url(self, url):
        self.URL = url
        self.Checker.Checks(self.URL)
        return self.Checker.CheckUrlRow()