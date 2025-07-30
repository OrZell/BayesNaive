from MainModel import MainModel

class Checker:

    def __init__(self, MainModel:MainModel, url):
        self.Model = MainModel
        self.URL = url.split(',')
        self.itemsList = []

    def Checks(self):
        # lenRow = len(self.URL)
        # lenExempleRow = len(self.Model.AllRelevantColumns)
        # if (lenRow != lenExempleRow) & (lenRow - 1 != lenExempleRow) & (lenRow != lenExempleRow - 1):
        #     raise 'Not Valid Input'

        for i in range(len(self.URL)):
            try:
                kind = type(self.Model.ExempleRow[i])
                self.itemsList.append(kind(self.URL[i]))
            except:
                self.itemsList.append(self.URL[i])

    def CheckUrlRow(self):

        AllPrecents = self.Model.GetTheModel()
        AllColumns = self.Model.AllRelevantColumns
        ALltablesLen = self.Model.AllTablesLen
        LenOfPrimaryTable = self.Model.LenOfPrimaryTable
        answers = {}

        for Unique in AllPrecents:
            num = 1
            i = 0
            while i < len(self.itemsList):
                num = num * AllPrecents[Unique][AllColumns[i]][0][self.itemsList[i]]
                i += 1
            num = num * ALltablesLen[Unique] / LenOfPrimaryTable
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1]