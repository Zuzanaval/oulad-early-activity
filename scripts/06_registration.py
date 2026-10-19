from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"

reg = pd.read_csv(DATA / "studentRegistration.csv")

print(reg.shape)
print(reg.head())
print(reg.isna().sum())

print(((reg["date_unregistration"]>=0)&(reg["date_unregistration"]<28)).sum())

