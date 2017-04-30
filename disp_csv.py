#! /usr/bin/env python3

import pandas as pd
# import sklearn
from sklearn.ensemble import RandomForestClassifier

n = 2000
nt = 285
nb_iter = 1
# test = pd.read_csv("data/test_short.csv").drop("sample_id", axis=1)
data = pd.read_csv('data/train.csv')
data = data[data["user_id"] == 547]
s = len(data)
n = int(0.8*s)
nt = int(0.2*s)
print(s, n, nt)
is_listened = data["is_listened"].copy()
data = data.drop("is_listened", axis=1)
test = data.iloc[n:n+nt]
data = data.iloc[:n]
print(len(data))
print(len(test))
for j in range(10, 11, 1):
    total = 0
    for k in range(nb_iter):
        rfc = RandomForestClassifier(n_estimators=j)
        rfc.fit(data, is_listened.iloc[:n])

        result = rfc.predict(test)
        print(rfc.feature_importances_)

        somme = 0
        vp = 0
        fp = 0
        for i in range(len(result)):
            if result[i] == is_listened.iloc[n+i]:
                somme += 1
            if result[i] == 1:
                if is_listened.iloc[n+i] == 1:
                    vp += 1
                if is_listened.iloc[n+i] == 0:
                    fp += 1
        total += somme
    print(result)
    print(test)
    print(is_listened)
    print("#trees/forest : "+str(j)+"\tRatio : "+str(total/(nt*nb_iter))+"\tROC : "+str(vp/(vp+fp)))
# with open('data/train_short.csv', 'r') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     next(spamreader)
#     for row in spamreader:
