import glob
import os

import pandas as pd


def print_json(df: pd.DataFrame):
    print(df.to_json())


def load_data(dirctory="/work/data/input/"):
    files = glob.glob(os.path.join(dirctory, "*.csv")) + glob.glob(os.path.join(dirctory, "*.parquet"))
    assert len(files) > 0, "No files found in the input directory"
    assert len(files) < 2, "Multiple files input is not supported yet"
    file_name = files[0]
    if file_name.endswith(".csv"):
        df = pd.read_csv(file_name)
    elif file_name.endswith(".parquet"):
        df = pd.read_parquet(file_name)

    return df


def get_stats(df: pd.DataFrame):
    return df.describe()
