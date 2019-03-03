import numpy as np
import pandas as pd


def split_title_and_name(person: str):
    return person.split()[0] + ' ' + person.split()[-1]


def test1():
    people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
    print(list(map(split_title_and_name, people)))


def test2():
    people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
    for person in people:
        print(split_title_and_name(person) == (lambda p: p.split()[0] + ' ' + p.split()[-1])(person))
    print(list(map(split_title_and_name, people)) == list(map((lambda p: p.split()[0] + ' ' + p.split()[-1]), people)))


def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i * j)
    return lst


def test3():
    print(times_tables() == [i * j for i in range(10) for j in range(10)])

def test4():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    answer = [i + j + k + l for i in lowercase for j in lowercase for k in digits for l in digits]
    print(answer)

if __name__ == "__main__":
    test4()
