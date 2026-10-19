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

print(df.shape)
print(df.groupby("final_result")["early_clicks"].agg(["count", "mean", "median"]).round(1))

print(df.groupby("age_band")["early_clicks"].agg(["count", "mean", "median"]).round(1))

order = ["Withdrawn", "Fail", "Pass", "Distinction"]
by_clicks_by_result=(df.groupby("final_result")["early_clicks"].median().reindex(order))
by_clicks_by_result.plot(kind="bar", figsize=(8,5))
plt.title("Median early clicks by final result ")
plt.ylabel("Median clicks (first 4 weeks)")
plt.xlabel("Final result")
plt.tight_layout()
plt.savefig(OUT/ "median_clicks_by_result.png",dpi=150)
print("\nGraf uložený do outputs/median_clicks_by_result.png") 

df["no_activity"]=df["early_clicks"]==0
print((df.groupby("final_result")["no_activity"].mean()*100).round(1))