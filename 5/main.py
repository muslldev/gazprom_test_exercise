import pandas as pd

def create_dataframe() -> pd.DataFrame:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [None, 5, 6], 'c': [7, None, 9]})
    df2 = pd.DataFrame({'b': [4, 89, 87], 'c': [54, 8, 35], 'd': [10, 11, 12]})

    df3 = df1.fillna(df2).astype(int)

    print(df3)

if __name__ == '__main__':
    create_dataframe()