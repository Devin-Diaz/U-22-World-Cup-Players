import pandas as pd

# Will add an additional row to our data containing a placeholder image depending on the position of the player

forward_placeholder_image = 'https://png.pngtree.com/png-vector/20250909/ourlarge/pngtree-focused-footballer-silhouette-in-action-preparing-to-kick-the-ball-png-image_17376673.webp'
midfielder_placeholder_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1fYKIH5E1fNxH0__3pjZqBvRWEIttrUg4pGYlbeq6UQ&s=10'
defender_placeholder_image = 'https://png.pngtree.com/recommend-works/png-clipart/20250422/ourlarge/pngtree-silhouette-dribbling-football-player-png-image_16056964.png'
goalie_placeholder_image = 'https://www.citypng.com/public/uploads/preview/free-football-goal-keeper-black-silhouette-png-704081694878919l9wkwqlmuo.png'

def get_player_placeholder(position):
    if position == "FW":
        return forward_placeholder_image
    elif position == "MF":
        return midfielder_placeholder_image
    elif position == "DF":
        return defender_placeholder_image
    elif position == "GK":
        return goalie_placeholder_image
    else:
        return None

df = pd.read_csv('csv_data/first_draft_player_data.csv')
df["player_image_url"] = df["pos"].apply(get_player_placeholder)
df.to_csv("second_draft_with_pos_placeholders.csv", index=False)
