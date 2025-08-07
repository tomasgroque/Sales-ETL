import pandas as pd 

def clean_data(df):
    df = df.drop_duplicates()

    df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    df.columns = df.columns.str.lower().str.replace(' ', '_')