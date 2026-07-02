"""
Script that parses out U-22 player information particpating in the FIFA World Cup 2026
"""

import pdfplumber
import pandas as pd
import re
from datetime import datetime

pdf_path = 'WC_Squads_List.pdf'

columns = [
    "#", "pos", "player_name", "first_names", "last_names",
    "name_on_shirt", "dob", "club", "height_cm", "caps", "goals"
]

all_players = []

def extract_country_details(page_text, page_num) -> list[str]:
    match = re.search(r"^(.+?)\s+\(([A-Z]{3})\)", page_text, re.MULTILINE)

    if not match:
        print(f"** Unable to extract country name & code on page: {page_num}. **")
        return None

    return [match.group(1).strip(), match.group(2).strip()]


def player_age(dob: str) -> int:
    dob_contents = dob.strip().split('/')
    cast_dob_contents = [int(item) for item in dob_contents]
    player_day, player_month, player_year = cast_dob_contents
    
    now = datetime.now()
    current_day, current_month, current_year = int(now.strftime("%d")), int(now.strftime("%m")), int(now.strftime("%Y"))

    age = current_year - player_year - ((current_month, current_day) < (player_month, player_day))

    return age


def under_22(age) -> bool:
    return True if age < 22 else False


with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        
        text = page.extract_text()
        country_details = extract_country_details(text, page_num)

        if country_details is None:
            continue

        country_name, country_code = country_details

        table = page.extract_table()

        for row in table[1:27]:
            row = [cell for cell in row if cell is not None]

            if len(row) != len(columns):
                print(f"** Skipping bad row on page: {page_num}. **")
                continue

            dob_info = row[6]

            age = player_age(dob_info)

            if not under_22(age):
                continue
            
            player = dict(zip(columns, row))
            player["country"] = country_name
            player["country_code"] = country_code
            player["age"] = age

            all_players.append(player)

df = pd.DataFrame(all_players)

df = df[
    ["country", "country_code", "#", "pos", "player_name", "first_names",
     "last_names", "name_on_shirt", "dob", "age", "club", "height_cm", "caps", "goals"]
]

df.to_csv("world_cup_squads.csv", index=False)

print(df.head())
print(df.shape)
