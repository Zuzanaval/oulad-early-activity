from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"
OUT = BASE / "outputs"

info = pd.read_csv(DATA / "studentInfo.csv")

# 1. chýbajúce hodnoty
print("Chýbajúce hodnoty:")
print(info.isna().sum())

# 2. opakujú sa študenti?
print("\nRiadkov:", len(info))
print("Unikátnych študentov:", info["id_student"].nunique())

# 3. výsledky v percentách
print("\nVýsledky (%):")
print((info["final_result"].value_counts(normalize=True) * 100).round(1))

# 4. výsledky podľa modulu v percentách
by_module = (pd.crosstab(info["code_module"], info["final_result"], normalize="index") * 100).round(1)
print("\nVýsledky podľa modulu (%):")
print(by_module)

# 5. graf
by_module.plot(kind="bar", stacked=True, figsize=(8, 5))
plt.title("Final result by module (%)")
plt.ylabel("% of students")
plt.xlabel("Module")
plt.legend(title="Final result", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig(OUT / "result_by_module.png", dpi=150)
print("\nGraf uložený do outputs/result_by_module.png")

print("\nVýsledky podľa pohlavia (%):")
print((info["gender"].value_counts(normalize=True) * 100).round(1))

by_age = (pd.crosstab(info["age_band"], info["final_result"], normalize="index") * 100).round(1)
print("\nVýsledky podľa vekovej skupiny (%):")
print(by_age)

by_age.plot(kind='bar', stacked=True,figsize=(8,5))
plt.title('Final result by age(%)')
plt.ylabel('% of students')
plt.xlabel('Age')
plt.legend(title='Final result according to age', bbox_to_anchor=(1.02,1), loc='upper left')
plt.tight_layout()
plt.savefig(OUT/'result_by_age.png', dpi=150)
print('\nGraf uložený do outputs/result_by_age.png')

print("\nPočet študentov pre každú vekovú skupinu:")
print(info["age_band"].value_counts())