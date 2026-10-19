from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"

vle = pd.read_csv(
    DATA / "studentVle.csv",
    usecols=["code_module", "code_presentation", "id_student", "date", "sum_click"],
    dtype={
        "code_module": "category",
        "code_presentation": "category",
        "id_student": "int32",
        "date": "int16",
        "sum_click": "int16",
    },
)

EARLY_DAYS = 28

early = vle[(vle["date"] >= 0) & (vle["date"] < EARLY_DAYS)]

early_clicks = (
    early.groupby(["code_module", "code_presentation", "id_student"], observed=True)["sum_click"]
    .sum()
    .reset_index(name="early_clicks")
)

print(early_clicks.shape)
print(early_clicks["early_clicks"].describe())

print((vle["date"]<0).sum())

OUT = Path(__file__).resolve().parent.parent / "outputs"
early_clicks.to_csv(OUT / "early_clicks.csv", index=False)