from AuxiFuncs import AuxiFuncs

class Classifier:

    def __init__(self):
        self.API_LINK = 'http://project-v2-backend:8000/'
        self.decode_dict = AuxiFuncs.decode_dict
        self.Reqs = AuxiFuncs.reqs
        self.AllPrecents = None
        self.AllColumns = None
        self.AllTablesLen = None
        self.LenOfPrimaryTable = None
        self.ExempleRow = None
        self.URL = None
        self.ItemsList = None


    def assign_values(self):
        self.AllPrecents = self.decode_dict(self.Reqs(self.API_LINK + 'GetTheModel'))
        self.AllColumns = self.decode_dict(self.Reqs(self.API_LINK + 'AllRelevantColumns'))
        self.AllTablesLen = self.decode_dict(self.Reqs(self.API_LINK + 'AllTablesLen'))
        self.LenOfPrimaryTable = self.decode_dict(self.Reqs(self.API_LINK + 'LenOfPrimaryTable'))
        self.ExempleRow = self.decode_dict(self.Reqs(self.API_LINK + 'ExempleRow'))

    def check_the_row_from_url(self, url):
        # lenRow = len(self.URL)
        # lenExempleRow = len(self.Model.AllRelevantColumns)
        # if (lenRow != lenExempleRow) & (lenRow - 1 != lenExempleRow) & (lenRow != lenExempleRow - 1):
        #     raise 'Not Valid Input'

        self.URL = url.split(',')
        self.ItemsList = []

        for i in range(len(self.URL)):
            try:
                kind = type(self.ExempleRow[i])
                self.ItemsList.append(kind(self.URL[i]))
            except:
                self.ItemsList.append(self.URL[i])

    def check_url_row(self):

        answers = {}

        for Unique in self.AllPrecents:
            num = 1
            i = 0
            while i < len(self.ItemsList):
                num = num * self.AllPrecents[Unique][self.AllColumns[i]][0][self.ItemsList[i]]
                i += 1
            num = num * self.AllTablesLen[Unique] / self.LenOfPrimaryTable
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1]