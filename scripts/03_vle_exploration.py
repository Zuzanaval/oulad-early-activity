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

print(vle.shape)
print(vle.head())
vle.info(memory_usage="deep")
print(vle.describe())

print(vle["date"].min())
print(vle["date"].max())