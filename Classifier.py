from Trainer import Trainer

class Classifier:

    def __init__(self, trainer:Trainer, url):
        self.Trainer = trainer
        self.URL = url.split(',')
        self.itemsList = []

    def check_the_types_of_url_items(self):
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

    def run_no_the_url(self):

        all_precents = self.Trainer.get_the_model()
        all_columns = self.Trainer.AllRelevantColumns
        all_tables_len = self.Trainer.AllTablesLen
        len_of_primary_table = self.Trainer.LenOfPrimaryTable
        answers = {}

        for Unique in all_precents:
            num = 1
            i = 0
            while i < len(self.itemsList):
                num = num * all_precents[Unique][all_columns[i]][0][self.itemsList[i]]
                i += 1
            num = num * all_tables_len[Unique] / len_of_primary_table
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1]