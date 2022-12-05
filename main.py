import numpy as np
import pandas as pd

# main program


data = './data/data.csv'
columns = ['Zaban', 'Khord', 'Kalan', 'Riazi', 'Amar', 'Doroos']
df = pd.read_csv(data, ',', header=0)


def mean(x):
    return round(np.mean(df[x]))


def std(x):
    return round(np.std(df[x]))


def minmax(mean, std):
    return regulator(str(mean - std)), regulator(str(mean + std)), regulator(str(mean))


def regulator(num):
    if len(num) == 1 and int(num) > 0:
        return ('0' + num)
    else:
        return num


def s_print(lessons, mean, minstd, maxstd, index):
    res = '{}. {}:\t{} <----({})----> {}'.format(index,
                                                 lessons, minstd, mean, maxstd)
    print(res)


def run():
    index = 0
    for lesson in columns:
        index += 1
        rmean = mean(lesson)
        rstd = std(lesson)
        minstd, maxstd, rmean = minmax(rmean, rstd)
        s_print(lesson, rmean, minstd, maxstd, index)


run()
