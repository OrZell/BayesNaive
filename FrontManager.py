from Classifier import Classifier

class FrontManager:

    def __init__(self):
        self.URL = None
        self.Checker = None

    def checker(self):
        self.Checker = Classifier()
        self.Checker.assign_values()

    def load_from_url(self, url):
        self.URL = url
        self.Checker.check_the_row_from_url(self.URL)
        return self.Checker.check_url_row()