import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import pandas as pd
from nflfunctions import get_all_players_by_position
# from nflfunctions import sum_player_stats_per_season
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

rb_data = df_games[df_games["player_id"].isin(rb_profiles["player_id"])]

rb_rushing_yards_df = sum_stats_per_grouping(rb_data, ['year', 'team'], ['rushing_yards'])
team_defensive_sacks = sum_stats_per_grouping(df_games, ['year', 'opponent'], ['defense_sacks'])

rb_rushing_yards_df = rb_rushing_yards_df[rb_rushing_yards_df["year"] > 1981]  # Sacks as an NFL stat only came into play after 1981
result_df = pd.merge(rb_rushing_yards_df, team_defensive_sacks, left_on=['team', 'year'], right_on=['opponent', 'year'])

sacks_result_df = result_df['defense_sacks']
rushing_yards_result_df = result_df["rushing_yards"]

_ = plt.plot(sacks_result_df, rushing_yards_result_df, linestyle='none', marker='.')
_ = plt.margins(0.02)
_ = plt.xlabel("sacks allowed per season")
_ = plt.ylabel("RB Rushing Yards Per Season")

a, b = np.polyfit(sacks_result_df, rushing_yards_result_df, 1)
# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

_ = plt.plot(x, y)
plt.show()
print(sacks_result_df.corr(rushing_yards_result_df))
