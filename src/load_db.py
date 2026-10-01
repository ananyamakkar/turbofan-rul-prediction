import sqlite3
from pathlib import Path

from src.data import load_split, load_rul

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DB = ROOT / "data" / "processed" / "engine.db"


def main():
    train = load_split(RAW / "train_FD001.txt")
    test = load_split(RAW / "test_FD001.txt")
    rul = load_rul(RAW / "RUL_FD001.txt")

    train["split"] = "train"
    test["split"] = "test"
    rul["unit"] = range(1, len(rul) + 1)

    DB.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB) as con:
        train.to_sql("readings", con, if_exists="replace", index=False)
        test.to_sql("readings", con, if_exists="append", index=False)
        rul.to_sql("test_rul", con, if_exists="replace", index=False)
        con.execute(
            "CREATE INDEX IF NOT EXISTS idx_readings ON readings(split, unit, cycle)"
        )
    print("Database written to", DB)


if __name__ == "__main__":
    main()