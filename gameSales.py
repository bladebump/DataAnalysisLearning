import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("vgsales.csv", index_col=0)[:1000]
    states = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    total = df.groupby('Name')[states].agg(np.sum).sort_values('Global_Sales',ascending=False)
    print(df.head())
