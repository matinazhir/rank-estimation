import numpy as np
import pandas as pd

# main program


data = './data/data.csv'
columns = ['Zaban', 'Khord', 'Kalan', 'Riazi', 'Amar', 'Doroos']
df = pd.read_csv(data, ',', header=0)


def minmax(mean, std):  # Calculate the standard range of data of a column
    return regulator(str(mean - std)), regulator(str(mean + std)), regulator(str(mean))


def regulator(num):
    """Make a 2 digits number
    For example if '5' is our number, it will change to '01'
    or if the number is '-5' or '55', It will remain as it is
    """
    if len(num) == 1 and int(num) > 0:
        return ('0' + num)
    else:
        return num


def s_print(lessons, mean, minstd, maxstd, index):  # It's a function for arrange a clean output
    res = '{}. {}:\t{} <----({})----> {}'.format(index,
                                                 lessons, minstd, mean, maxstd)
    print(res)


def run():
    index = 0
    for lesson in columns:
        index += 1  # indexing lessons
        rmean = round(np.mean(df[lesson]))  # rounded mean
        rstd = round(np.std(df[lesson]))  # rounded std
        minstd, maxstd, rmean = minmax(rmean, rstd)  # calculate standard range
        s_print(lesson, rmean, minstd, maxstd, index)  # print the output


run()
