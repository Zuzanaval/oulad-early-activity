from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"

info = pd.read_csv(DATA / "studentInfo.csv")

print(info.shape)
print(info.head())
info.info()
print(info["final_result"].value_counts())