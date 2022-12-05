import numpy as np
import pandas as pd


data = './data/data.csv'
columns = ['Zaban', 'Khord', 'Kalan', 'Riazi', 'Amar', 'Doroos']
df = pd.read_csv(data, ',', header=0)
zarib = [1, 4, 4, 2, 2, 3]
lessons = {}
# each key('lesson') has 3 values([mean, std, zarib])
[lessons.setdefault(lesson, []) for lesson in columns]

i = 0
for lesson in columns:
    lessons[lesson].append(round(np.mean(df[lesson])))
    lessons[lesson].append(round(np.std(df[lesson])))
    lessons[lesson].append(zarib[i])
    i += 1

res = []
for i in range(len(df.index)):
    temp = []
    for lesson in columns:
        z = (df.loc[i, lesson] - lessons[lesson][0])/lessons[lesson][1]
        t = (1000*z) + 5000
        temp.append(t*lessons[lesson][2])
    res.append((sum(temp)/sum(zarib))/df.loc[i, 'Taraz'])

newl = []
resm = np.mean(res)
ress = np.std(res)
for i in res:
    if i > (resm - ress) and i < (resm + ress):
        newl.append(i)

factor = sum(newl)/len(newl)
