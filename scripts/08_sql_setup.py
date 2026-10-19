from pathlib import Path
import sqlite3
import pandas as pd

OUT = Path(__file__).resolve().parent.parent / "outputs"

df = pd.read_csv(OUT / "student_early_activity.csv")

conn = sqlite3.connect(OUT / "oulad.db")
df.to_sql("student_early_activity", conn, if_exists="replace", index=False)

result = pd.read_sql("SELECT COUNT(*) AS n_rows FROM student_early_activity", conn)
print(result)

query = """
SELECT final_result, COUNT(*) AS n
FROM student_early_activity
GROUP BY final_result
"""

query = """
SELECT final_result,
       COUNT(*) AS n,
       ROUND(AVG(early_clicks), 1) AS avg_clicks
FROM student_early_activity
WHERE stayed_after_4w = 1
GROUP BY final_result
ORDER BY avg_clicks DESC
"""

query = """
SELECT code_module,
       CASE
           WHEN early_clicks = 0   THEN '0'
           WHEN early_clicks <= 50 THEN '1-50'
           WHEN early_clicks <= 200 THEN '51-200'
           WHEN early_clicks <= 500 THEN '201-500'
           ELSE '500+'
       END AS activity_group,
       CASE
           WHEN early_clicks = 0   THEN 1
           WHEN early_clicks <= 50 THEN 2
           WHEN early_clicks <=200 THEN 3
           WHEN early_clicks <=500 THEN 4
           ELSE 5
       END AS sort_order,
       COUNT(*) AS n,
       SUM(CASE WHEN final_result = 'Fail' THEN 1 ELSE 0 END) AS n_fail,
       SUM(CASE WHEN final_result = 'Withdrawn' THEN 1 ELSE 0 END)AS n_withdrawn
FROM student_early_activity
WHERE stayed_after_4w = 1
GROUP BY code_module, activity_group, sort_order
ORDER BY code_module, sort_order
"""
print(pd.read_sql(query, conn))



activity_by_module = pd.read_sql(query, conn)
print(activity_by_module.shape)
print(activity_by_module["n"].sum())
activity_by_module.to_csv(OUT / "activity_groups_by_module.csv", index=False)

conn.close()