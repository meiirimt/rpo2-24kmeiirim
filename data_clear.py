import pandas as pd

def load_file(path):
    if path.endswith('.csv'):
        return pd.read_csv(path)
    elif path.endswith('.json'):
        return pd.read_json(path)
    elif path.endswith('.txt'):
        return pd.read_csv(path, sep='\t')
    elif path.endswith('.xlsx'):
        return pd.read_excel(path)


def get_shape(df):
    return df.shape

def get_null_info(df):
    return df.isnull().sum()

def get_numeric_stats(df):
    return df.describe()

def get_top_values(df):
    result = {}
    for col in df.select_dtypes(include='object'):
        result[col] = df[col].value_counts().head(3)
    return result

def clean_data(df):

    for col in df.select_dtypes(include='object'):
        df[col] = df[col].fillna("Unknown").str.strip()

    df = df.drop_duplicates(subset='product_name')

    df = df.fillna(df.mean(numeric_only=True))

    return df