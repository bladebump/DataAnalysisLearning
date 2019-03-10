import pandas as pd
import numpy as np


def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data), 'std': np.std(data)})


def test1():
    df = pd.read_csv('data/census.csv')
    print(df.apply(min_max, axis=1))


def test2():
    df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                      index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor',
                             'poor'])
    df.rename(columns={0: 'Grades'}, inplace=True)
    # grades = df['Grades'].astype('category',
    #                              categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
    #                              ordered=True)
    grades = pd.Categorical(df['Grades'], categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                            ordered=True)
    print(grades)


def test3():
    s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
    print(pd.cut(s, 3, labels=['Small', 'Medium', 'Large']))


if __name__ == "__main__":
    test3()
