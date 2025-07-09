import pandas as pd
import copy

PrimaryTable = pd.read_csv('DemoPhishing.csv')
PrimaryTableLen = PrimaryTable.shape[0]
TargetColumn = PrimaryTable.columns.tolist()[-1]
uniquesTargets = PrimaryTable[TargetColumn].unique().tolist()
allColumns = PrimaryTable.columns.tolist()[1:-1]

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
            AllPrecents[Target][Column][0][Unique] = float(precents)

print(AllPrecents)
print(AllPrecentsPre)

age = input('enter age:')
income = input('enter income:')
student = input('enter student:')
rating = input('enter rating:')

CheckTheRow = PrimaryTable[(PrimaryTable[allColumns[0]] == age) & (PrimaryTable[allColumns[1]] == income) & (PrimaryTable[allColumns[2]] == student) & (PrimaryTable[allColumns[3]] == rating)].index.tolist()
if CheckTheRow:
    print('Contained')
    print(PrimaryTable.loc[CheckTheRow[0]][TargetColumn])
else:
    print('Not Contained')
    PrecentsByTarget = {}
    for uniqueTarget in uniquesTargets:
        num = AllPrecents[uniqueTarget][allColumns[0]][0][age]
        num = num * AllPrecents[uniqueTarget][allColumns[1]][0][income]
        num = num * AllPrecents[uniqueTarget][allColumns[2]][0][student]
        num = num * AllPrecents[uniqueTarget][allColumns[3]][0][rating]
        num = num * AllTablesLen[uniqueTarget] / PrimaryTableLen
        PrecentsByTarget[uniqueTarget] = num

    sorted_dict = dict(sorted(PrecentsByTarget.items(), key=lambda item: item[1]))
    print(sorted_dict)