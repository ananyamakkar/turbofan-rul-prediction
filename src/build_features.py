import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "processed" / "engine.db"

SENSORS = ["s_2", "s_3", "s_4", "s_7", "s_8", "s_9", "s_11",
           "s_12", "s_13", "s_14", "s_15", "s_17", "s_20", "s_21"]
WINDOW = 5  # rolling-average length in cycles


def main():
    raw_cols = ", ".join(SENSORS)
    avg_cols = ", ".join(
        f"AVG({s}) OVER (PARTITION BY split, unit ORDER BY cycle "
        f"ROWS BETWEEN {WINDOW - 1} PRECEDING AND CURRENT ROW) AS {s}_avg{WINDOW}"
        for s in SENSORS
    )
    with sqlite3.connect(DB) as con:
        con.execute("DROP TABLE IF EXISTS features")
        con.execute(f"""
            CREATE TABLE features AS
            SELECT
                split, unit, cycle,
                CASE WHEN split = 'train'
                     THEN MAX(cycle) OVER (PARTITION BY split, unit) - cycle
                END AS rul,
                {raw_cols},
                {avg_cols}
            FROM readings
        """)
        n = con.execute("SELECT COUNT(*) FROM features").fetchone()[0]
    print(f"features table rebuilt: {n} rows")


if __name__ == "__main__":
    main()