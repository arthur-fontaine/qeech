import os
import pandas as pd


def load_data(data_path: str):
    data = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", f"{data_path}.csv"))
    return data
