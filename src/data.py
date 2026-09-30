import pandas as pd

INDEX_COLS = ["unit", "cycle"]
SETTING_COLS = [f"setting_{i}" for i in range(1, 4)]
SENSOR_COLS = [f"s_{i}" for i in range(1, 22)]
ALL_COLS = INDEX_COLS + SETTING_COLS + SENSOR_COLS

def load_split(path):
    return pd.read_csv(path, sep=r"\s+", header=None, names=ALL_COLS)

def load_rul(path):
    return pd.read_csv(path, header=None, names=["rul"])
