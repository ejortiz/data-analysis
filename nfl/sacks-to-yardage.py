import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from nflfunctions import get_all_players_by_position
from nflfunctions import sum_player_stats_per_season
from nflfunctions import sum_stats_per_grouping

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

print(df_games.info())
rb_data = df_games[df_games["player_id"].isin(rb_profiles["player_id"])]

rb_rushing_yards_df = sum_player_stats_per_season(rb_data, ['rushing_yards'])
team_defensive_sacks = sum_stats_per_grouping(df_games, ['year', 'opponent'], ['defense_sacks'])

# result_df = pd.merge(rb_rushing_yards_df, team_defensive_sacks, left_on='team', right_on='opponent')
indexed_rb_df = rb_rushing_yards_df.stack().reset_index()
indexed_sacks_df = team_defensive_sacks.stack().reset_index()

# print(indexed_rb_df.info())
# print(indexed_sacks_df.info())

result_df = pd.merge(indexed_rb_df, indexed_sacks_df, left_on=['team', 'year'], right_on=['opponent', 'year'])
# print(result_df.info())
print(result_df.head())


_ = plt.plot(result_df['0_y'], result_df['0_x'], linestyle='none', marker = '.')
_ = plt.margins(0.02)
_ = plt.xlabel("sacks per season")
_ = plt.ylabel("RB Rushing Yards Per Season")
plt.show()

# print(result_df)