import pandas as pd
import copy

first_file = pd.read_csv('Data/phishing.csv', index_col='Index').dropna().drop_duplicates().reset_index(drop=True)
print(first_file.shape)

PrimaryTable = first_file[first_file.index < 0.7*len(first_file)]
PrimaryTableLen = PrimaryTable.shape[0]
TargetColumn = PrimaryTable.columns.tolist()[-1]
uniquesTargets = PrimaryTable[TargetColumn].unique().tolist()
allColumns = PrimaryTable.columns.tolist()[:-1]

AllPrecents = {}
AllTables = {}
AllTablesLen = {}

for unique in uniquesTargets:
    AllPrecents[unique] = {}
    AllTables[unique] = PrimaryTable[PrimaryTable[TargetColumn] == unique]
    AllTablesLen[unique] = AllTables[unique].shape[0]

flag = False

for uniquePrime in uniquesTargets:
    for col in allColumns:
        AllPrecents[uniquePrime][col] = [{}]
        uniques = PrimaryTable[col].unique().tolist()
        for unique in uniques:
            listCount = PrimaryTable[PrimaryTable[TargetColumn] == uniquePrime][col].tolist()
            counts = listCount.count(unique)
            if counts == 0:
                flag = True
            AllPrecents[uniquePrime][col][0][unique] = counts
        AllPrecents[uniquePrime][col].append(AllTablesLen[uniquePrime])

if flag:
    for Target in AllPrecents:
        for Column in AllPrecents[Target]:
            if 0 in AllPrecents[Target][Column][0].values():
                for var in AllPrecents[Target][Column][0]:
                    AllPrecents[Target][Column][0][var] += 1
                AllPrecents[Target][Column][1] += 1



AllPrecentsPre = copy.deepcopy(AllPrecents)


for Target in AllPrecents:
    for Column in AllPrecents[Target]:
        for Unique in AllPrecents[Target][Column][0]:
            precents = AllPrecents[Target][Column][0][Unique] / AllPrecents[Target][Column][1]
            AllPrecents[Target][Column][0][Unique] = precents

print(AllPrecents)
print(AllPrecentsPre)

FileToCheck = first_file[first_file.index >= 0.7 * len(first_file)]
fileRows = FileToCheck.drop(FileToCheck.columns[-1], axis=1).values.tolist()
rightAnswers = FileToCheck[FileToCheck.columns[-1]].tolist()

print(len(allColumns), len(fileRows[0]))
answers = []
for row in fileRows:
    PrecentsByTarget = {}
    for uniqueTarget in uniquesTargets:
        num = 1
        for i in range(len(row)):
            num = num * AllPrecents[uniqueTarget][allColumns[i]][0][row[i]]
        num = num * AllTablesLen[uniqueTarget] / PrimaryTableLen
        PrecentsByTarget[uniqueTarget] = num
    sorted_dict = list(dict(sorted(PrecentsByTarget.items(), key=lambda item: item[1])).keys())
    answers.append(sorted_dict[1])

print(rightAnswers)
print(answers)
depends = []
for i in range(len(rightAnswers)):
    if rightAnswers[i] == answers[i]:
        depends.append(True)
    else:
        depends.append(False)

print(depends.count(True) / len(depends))