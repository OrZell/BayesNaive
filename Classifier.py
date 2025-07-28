from Trainer import Trainer

class Classifier:

    def __init__(self, trainer:Trainer, url):
        self.Trainer = trainer
        self.URL = url.split(',')
        self.itemsList = []
        self.AllPrecents = None
        self.AllColumns = None
        self.AllTablesLen = None
        self.LenOfPrimaryTable = None

    def check_validate_the_url(self):
        # lenRow = len(self.URL)
        # lenExempleRow = len(self.Model.AllRelevantColumns)
        # if (lenRow != lenExempleRow) & (lenRow - 1 != lenExempleRow) & (lenRow != lenExempleRow - 1):
        #     raise 'Not Valid Input'

        for i in range(len(self.URL)):
            try:
                kind = type(self.Trainer.ExempleRow[i])
                self.itemsList.append(kind(self.URL[i]))
            except:
                self.itemsList.append(self.URL[i])

    def check_url_as_row(self):

        self.AllPrecents = self.Trainer.get_the_model()
        self.AllColumns = self.Trainer.AllRelevantColumns
        self.AllTablesLen = self.Trainer.AllTablesLen
        self.LenOfPrimaryTable = self.Trainer.LenOfPrimaryTable
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