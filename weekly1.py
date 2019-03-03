import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), index=list(range(4)), columns=['a', 'b', 'c', 'd'])
    print(df.loc[:, 'a':'c'])
