import numpy as np
import pandas as pd


data = './data/data.csv'
columns = ['Zaban', 'Khord', 'Kalan', 'Riazi', 'Amar', 'Doroos']
df = pd.read_csv(data, ',', header=0)


def minmax(mean, std):  # Calculate the standard range of data of a column
    low = regulator(str(mean - std))
    high = regulator(str(mean + std))
    center = regulator(str(mean))
    return low, high, center


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
        rmean = round(np.mean(df[lesson]))  # Calculate rounded mean (average)
        # Calculate rounded standard deviation (std)
        rstd = round(np.std(df[lesson]))
        minstd, maxstd, rmean = minmax(rmean, rstd)  # Calculate standard range
        s_print(lesson, rmean, minstd, maxstd, index)  # Print the output


run()
