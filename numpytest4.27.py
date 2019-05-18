import numpy as np
import matplotlib.pyplot as plt

splite_out = lambda: print("----------------------")


def test1():
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    print(arr)
    print(arr[[4, 3, 0, 6]])  # 子集序列索引
    print(arr[[-1, -5, 7]])
    splite_out()
    arr = np.arange(32).reshape((8, 4))
    print(arr)
    print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
    splite_out()
    print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])


def test2():
    arr = np.arange(16).reshape((2, 2, 4))
    print(arr)
    splite_out()
    print(arr.transpose((1, 0, 2)))  # 换轴
    splite_out()
    print(arr.swapaxes(1, 2))


def test3():
    point = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(point, point)
    print(xs)
    splite_out()
    print(ys)
    splite_out()
    z = np.sqrt(xs ** 2 + ys ** 2)
    print(z)
    plt.imshow(z, cmap=plt.cm.gray)
    plt.title("Image plot of $\sqrt{x^2+y^2}$ for grid of values")
    plt.show()


def test4():
    arr = np.random.randn(4, 4)
    print(arr)
    splite_out()
    print(np.where(arr > 0, 2, -2))


def test5():
    arr = np.random.randn(100)
    print((arr > 0).sum())
    print((arr > 0).any())  # 是否有true
    print((arr > 0).all())  # 是否全为0


def test6():
    names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
    print(np.unique(names))  # 去重
    splite_out()
    values = [6, 0, 0, 3, 2, 5, 6]
    print(np.in1d(values, [2, 3, 6]))  # 检查元素是否在另一个数组中


def test7():
    arr = np.arange(10)
    np.savez("data/some_arr.npz", a=arr, b=arr ** 2)
    load_arr = np.load("data/some_arr.npz")
    print(load_arr['a'])
    print(load_arr['b'])


def test8():
    nstep = 1000
    draws = np.random.randint(0, 2, size=nstep)
    print(draws)
    splite_out()
    steps = np.where(draws > 0, 1, -1)
    print(steps)
    splite_out()
    walk = steps.cumsum()
    print(walk)
    splite_out()
    print(walk.max())
    print(walk.min())
    splite_out()
    print(walk[walk > 9])


if __name__ == "__main__":
    test8()
