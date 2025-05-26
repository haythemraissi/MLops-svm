import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    if 'Unnamed: 32' in df.columns:
        df.drop(columns=['Unnamed: 32'], inplace=True)
    if 'id' in df.columns:
        df.drop(columns=['id'], inplace=True)
    df.dropna(inplace=True)
    return df
