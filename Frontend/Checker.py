import requests
import json

class Checker:

    def __init__(self):
        self.API_LINK = 'http://backend:8000/'


    def decode_dict(self, d: dict):

        def decode_key(k):
            key_info = json.loads(k)
            raw = key_info["__key__"]
            t = key_info["__type__"]
            if t == "int":
                return int(raw)
            elif t == "float":
                return float(raw)
            elif t == "bool":
                return raw == "True"
            else:
                return raw  # str

        def decode_item(obj):
            if isinstance(obj, dict):
                return {decode_key(k): decode_item(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [decode_item(x) for x in obj]
            else:
                return obj

        return decode_item(d)

    def assign(self):
        self.AllPrecents = self.decode_dict(self.Reqs('GetTheModel'))
        self.AllColumns = self.decode_dict(self.Reqs('AllRelevantColumns'))
        self.AllTablesLen = self.decode_dict(self.Reqs('AllTablesLen'))
        self.LenOfPrimaryTable = self.decode_dict(self.Reqs('LenOfPrimaryTable'))
        self.exmpleRow = self.decode_dict(self.Reqs('ExempleRow'))


    def Reqs(self, resource):
        url = self.API_LINK + resource
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            return response.json()
        else:
            raise 'Err'

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