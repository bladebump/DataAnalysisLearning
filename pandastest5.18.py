import numpy as np
import pandas as pd
import pandas_datareader as web

split_output = lambda: print("--------------------")


def test1():
    df = pd.DataFrame(np.random.randn(12).reshape((3, 4)), index=list('abc'), columns=list('abcd'))
    print(df)
    split_output()
    print(df.sum())
    split_output()
    print(df.sum(axis='columns'))
    split_output()
    print(df.mean())
    split_output()
    print(df.idxmax())
    split_output()
    print(df.idxmin())
    split_output()
    print(df.cumsum())
    split_output()
    print(df.describe())
    split_output()


def test2():
    all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
    price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
    volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})
    returns = price.pct_change()
    print(returns.tail())
    split_output()
    print(returns['MSFT'].corr(returns['IBM']))
    split_output()
    print(returns['MSFT'].cov(returns['IBM']))
    split_output()
    print(returns.MSFT.corr(returns.IBM))
    split_output()
    print(returns.corr())
    split_output()
    print(returns.cov())
    split_output()
    print(returns.corrwith(returns.IBM))
    split_output()
    return all_data, price, volume


if __name__ == "__main__":
    a, b, c = test2()
