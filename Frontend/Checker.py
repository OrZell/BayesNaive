import requests

class Checker:

    def __init__(self):
        self.API_LINK = 'http://127.0.0.1:8000/'

    def assign(self):
        self.AllPrecents = self.Reqs('GetTheModel')
        self.AllColumns = self.Reqs('AllRelevantColumns')
        self.AllTablesLen = self.Reqs('AllTablesLen')
        self.LenOfPrimaryTable = self.Reqs('LenOfPrimaryTable')
        self.exmpleRow = self.Reqs('ExempleRow')


    def Reqs(self, resource):
        url = self.API_LINK + resource
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            return response.json()
        else:
            raise 'Err'

    # def Checks(self):
    #     # lenRow = len(self.URL)
    #     # lenExempleRow = len(self.Model.AllRelevantColumns)
    #     # if (lenRow != lenExempleRow) & (lenRow - 1 != lenExempleRow) & (lenRow != lenExempleRow - 1):
    #     #     raise 'Not Valid Input'
    #
    #     exmpleRow = self.Reqs('ExempleRow')
    #
    #     for i in range(len(self.URL)):
    #         try:
    #             kind = type(exmpleRow[i])
    #             self.itemsList.append(kind(self.URL[i]))
    #         except:
    #             self.itemsList.append(self.URL[i])

    def Checks(self, url):
        self.URL = url.split(',')
        self.itemsList = []
        for i in range(len(self.URL)):
            example_val = self.exmpleRow[i]
            example_type = type(example_val)

            try:
                if example_type == bool:
                    val = self.URL[i].strip().lower() in ['true', '1', 'yes']
                elif example_type == int:
                    val = int(float(self.URL[i]))  # תמיכה גם ב"5.0"
                elif example_type == float:
                    val = float(self.URL[i])
                else:
                    val = example_type(self.URL[i])
            except:
                val = self.URL[i]

            self.itemsList.append(val)

    def CheckUrlRow(self):

        answers = {}

        for Unique in self.AllPrecents:
            num = 1
            i = 0
            while i < len(self.itemsList):
                print(f"{Unique}")
                print(f"{self.AllColumns[i]}")
                print(f"{self.itemsList[i]}")
                print(self.AllPrecents)
                one = self.AllPrecents[Unique]
                two = one[self.AllColumns[i]][0]
                three = two[str(self.itemsList[i])]
                # num = num * self.AllPrecents[Unique][self.AllColumns[i]][0][self.itemsList[i]]
                num = num * three
                print(num)
                i += 1
            num = num * self.AllTablesLen[Unique] / self.LenOfPrimaryTable
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1]