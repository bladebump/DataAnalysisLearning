import pandas as pd
import numpy as np

splite_out = lambda: print("----------------------")


def test1():
    obj = pd.Series([4, 7, -5, 3])
    print(obj)
    splite_out()
    print(obj.values)
    splite_out()
    print(obj.index)
    splite_out()
    obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    print(obj2)
    splite_out()
    print(obj2.index)
    splite_out()
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = pd.Series(sdata)
    print(obj3)
    splite_out()
    states = ['California', 'Ohio', 'Oregon', 'Texas']
    obj4 = pd.Series(sdata, index=states)
    print(obj4)
    splite_out()
    print(pd.isnull(obj4))  # obj4.isnull
    splite_out()
    print(pd.notnull(obj4))  # obj4.notnull
    splite_out()
    print(obj3 + obj4)
    splite_out()
    obj4.name = 'population'
    obj4.index.name = 'state'
    print(obj4)
    splite_out()
    obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
    print(obj)
    splite_out()


def test2():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    print(frame)
    splite_out()
    print(frame.head())
    splite_out()
    print(pd.DataFrame(data, columns=['year', 'state', 'pop']))
    splite_out()
    frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                          index=['one', 'two', 'three', 'four', 'five', 'six'])
    print(frame2)
    splite_out()
    print(frame2.values)
    splite_out()


def test3():
    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    print(obj)
    splite_out()
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    print(obj2)
    obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
    print(obj3)
    splite_out()
    print(obj3.reindex(range(6), method='ffill'))
    splite_out()
    frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=[chr(i + ord('a')) for i in range(3)],
                         columns=['Ohio', 'Texas', 'California'])
    print(frame)
    splite_out()
    print(frame.reindex(['a', 'b', 'c', 'd']))
    splite_out()
    states = ['Texas', 'Utah', 'California']
    print(frame.reindex(columns=states))
    splite_out()
    print(frame.reindex(['a', 'b', 'c', 'd'], columns=states))


if __name__ == "__main__":
    test3()
