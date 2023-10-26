import os
import polars as pl


def load_data(data_path: str):
    data = pl.read_csv(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", f"{data_path}.csv"))
    return data
