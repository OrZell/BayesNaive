from Classifier import Classifier

class FrontManager:

    def __init__(self):
        self.URL = None
        self.Checker = None

    def checker(self):
        self.Checker = Classifier()
        self.Checker.assign()

    def load_from_url(self, url):
        self.URL = url
        self.Checker.Checks(self.URL)
        return self.Checker.CheckUrlRow()