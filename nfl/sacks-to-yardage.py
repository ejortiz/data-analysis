import numpy as np
import pandas as pd
from nflfunctions import get_all_players_by_position

import os
file_path = os.path.dirname(os.path.abspath(__file__))
player_stats_file = 'nfl_profiles.csv'
games_file = 'nfl_games.csv'
player_stats_full_path = file_path + '\\nfl_profiles.csv'
games_full_path = file_path + '\\nfl_games.csv'

# get all running back profiles
df_profiles = pd.read_csv(player_stats_full_path)
# df_profiles.set_index("Unnamed: 0")
rb_profiles = get_all_players_by_position(df_profiles, 'RB')

df_games = pd.read_csv(games_full_path)
rb_data = df_games[df_games["player_id"].isin(rb_profiles["player_id"])]

