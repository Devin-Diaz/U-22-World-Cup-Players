import json
import pandas as pd

input_path = 'ETL/data/final_draft.csv'
df = pd.read_csv(input_path)

df["flag_colors"] = df["flag_colors"].apply(json.loads)
records = df.to_dict(orient = "records")

with open("final_draft.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4, ensure_ascii=False)