import pandas as pd
import numpy as np

splite_outpu = lambda: print("--------------------")


def test1():
    obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    print(obj)
    splite_outpu()
    new_obj = obj.drop('c')
    print(new_obj)
    splite_outpu()
    print(obj.drop(['d', 'c']))
    splite_outpu()
    data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                        columns=['one', 'two', 'three', 'four'])
    print(data)
    splite_outpu()
    print(data.drop(['Colorado', 'Ohio']))
    splite_outpu()
    print(data.drop(['two'], axis=1))
    splite_outpu()


def test2():
    s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
    s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
    print(s1)
    splite_outpu()
    print(s2)
    splite_outpu()
    print(s1 + s2)
    splite_outpu()
    df1 = pd.DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
    df2 = pd.DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))
    df2.loc[1, 'b'] = np.nan
    print(df1 + df2)
    splite_outpu()
    print(df1.add(df2, fill_value=0))
    splite_outpu()


def test3():
    arr = np.arange(12.).reshape((3, 4))
    print(arr)
    splite_outpu()
    print(arr[0])
    splite_outpu()
    print(arr - arr[0])
    splite_outpu()
    frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=list('abcd'))
    series = frame.iloc[0]
    print(frame)
    splite_outpu()
    print(series)
    splite_outpu()
    print(frame - series)
    splite_outpu()
    series3 = frame['d']
    print(series)
    splite_outpu()
    print(frame.sub(series3, axis='index'))


def test4():
    frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=list('abcd'))
    print(frame)
    splite_outpu()
    print(np.abs(frame))
    splite_outpu()
    f = lambda x: x.max() - x.min()
    print(frame.apply(f))
    splite_outpu()
    print(frame.apply(f, axis='columns'))
    splite_outpu()
    format = lambda x: '%.2f' % x
    print(frame.applymap(format))
    splite_outpu()


def test5():
    obj = pd.Series(range(4), index=list('dabc'))
    print(obj.sort_index())
    splite_outpu()
    frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=list('dabc'))
    print(frame.sort_index())
    splite_outpu()
    print(frame.sort_index(axis='columns'))
    splite_outpu()
    obj2 = pd.Series([4, np.nan, 7, -3, np.nan, 2])
    print(obj2.sort_values())
    splite_outpu()
    print(obj2.sort_values(ascending=False))


if __name__ == "__main__":
    test5()
