from MainModel import MainModel

class urlReader:

    def __init__(self, MainModel:MainModel):
        self.Model = MainModel

    def CheckUrlRow(self, url):
        url = url.split(',')
        url = [int(x) for x in url]
        AllPrecents = self.Model.GetTheModel()
        AllColumns = self.Model.AllRelevantColumns
        ALltablesLen = self.Model.AllTablesLen
        LenOfPrimaryTable = self.Model.LenOfPrimaryTable
        answers = {}

        for Unique in AllPrecents:
            num = 1
            for i in range(len(url)):
                num = num * AllPrecents[Unique][AllColumns[i]][0][url[i]]
            print(ALltablesLen[Unique])
            num = num * ALltablesLen[Unique] / LenOfPrimaryTable
            answers[Unique] = num
        sorted_dict = list(dict(sorted(answers.items(), key=lambda item: item[1])).keys())
        return sorted_dict[-1]