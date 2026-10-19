from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"
OUT = BASE / "outputs"

info = pd.read_csv(DATA / "studentInfo.csv")
early = pd.read_csv(OUT / "early_clicks.csv")

keys = ["code_module", "code_presentation", "id_student"]
df = info.merge(early, on=keys, how="left")
df["early_clicks"] = df["early_clicks"].fillna(0)

reg = pd.read_csv(DATA / "studentRegistration.csv")
df = df.merge(reg[keys + ["date_unregistration"]], on=keys, how="left")
print(df.shape)



#print(((reg["date_unregistration"]>=0)&(reg["date_unregistration"]<28)).sum())

stayed = df[(df["date_unregistration"].isna()) | (df["date_unregistration"] >= 28)]
print(len(stayed))

print(stayed.groupby("final_result")["early_clicks"].agg(["count", "mean", "median"]).round(1))

stayed = stayed.copy()
stayed["no_activity"] = stayed["early_clicks"] == 0
print((stayed.groupby("final_result")["no_activity"].mean() * 100).round(1))


df["stayed_after_4w"] = df["date_unregistration"].isna() | (df["date_unregistration"] >= 28)
df["no_activity"] = df["early_clicks"] == 0
df.to_csv(OUT / "student_early_activity.csv", index=False)
print(df.shape)