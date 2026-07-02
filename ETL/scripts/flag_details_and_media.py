import pandas as pd
import json

def normalize_country_name(name: str) -> str:
    return str(name).lower().strip()

def enrich_with_flag_data(players_csv, flag_colors_json, flag_codes_json, output_csv):

    df = pd.read_csv(players_csv)

    with open(flag_colors_json, "r", encoding='utf-8') as f:
        flag_colors = json.load(f)
    
    with open(flag_codes_json, "r", encoding="utf-8") as f:
        flag_codes = json.load(f)
    
    # Reverse country code and name e.g {"Argentina": "AR",...}
    country_to_code = {
        normalize_country_name(country): code.upper()
        for code, country in flag_codes.items()
    }

    country_to_colors = {
        normalize_country_name(item["name"]): item.get("colors", [])
        for item in flag_colors
    }

    df["flag_code"] = df["country"].apply(
        lambda country: country_to_code.get(normalize_country_name(country))
    )

    df["flag_url"] = df["flag_code"].apply(
        lambda code: f"https://flagsapi.com/{code}/flat/64.png" if pd.notna(code) else None
    )

    df["flag_colors"] = df["country"].apply(
        lambda country: json.dumps(country_to_colors.get(normalize_country_name(country), []))
    )

    df.to_csv(output_csv, index=False)


player_csv = 'csv_data/second_draft_with_pos_placeholders.csv'
flag_colors = 'flag_colors.json'
flag_codes = 'flag_codes.json'
output_csv = 'third_draft_with_flag_data.csv'
enrich_with_flag_data(player_csv, flag_colors, flag_codes, output_csv)

    



