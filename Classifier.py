from AuxiFuncs import AuxiFuncs

class Classifier:

    def __init__(self):
        self.API_LINK = 'http://backend:8000/'
        self.decode_dict = AuxiFuncs.decode_dict
        self.Reqs = AuxiFuncs.Reqs

    def assign(self):
        self.AllPrecents = self.decode_dict(self.Reqs(self.API_LINK + 'GetTheModel'))
        self.AllColumns = self.decode_dict(self.Reqs(self.API_LINK + 'AllRelevantColumns'))
        self.AllTablesLen = self.decode_dict(self.Reqs(self.API_LINK + 'AllTablesLen'))
        self.LenOfPrimaryTable = self.decode_dict(self.Reqs(self.API_LINK + 'LenOfPrimaryTable'))
        self.exmpleRow = self.decode_dict(self.Reqs(self.API_LINK + 'ExempleRow'))

    def Checks(self, url):
        # lenRow = len(self.URL)
        # lenExempleRow = len(self.Model.AllRelevantColumns)
        # if (lenRow != lenExempleRow) & (lenRow - 1 != lenExempleRow) & (lenRow != lenExempleRow - 1):
        #     raise 'Not Valid Input'

        self.URL = url.split(',')
        self.itemsList = []
        exmpleRow = self.Reqs('ExempleRow')

        for i in range(len(self.URL)):
            try:
                kind = type(exmpleRow[i])
                self.itemsList.append(kind(self.URL[i]))
            except:
                self.itemsList.append(self.URL[i])

    def CheckUrlRow(self):

        answers = {}

        for Unique in self.AllPrecents:
            num = 1
            i = 0
            while i < len(self.itemsList):
                num = num * self.AllPrecents[Unique][self.AllColumns[i]][0][self.itemsList[i]]
                i += 1
            num = num * self.AllTablesLen[Unique] / self.LenOfPrimaryTable
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1]