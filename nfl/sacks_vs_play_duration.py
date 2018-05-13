import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import pandas as pd
from nflfunctions import get_all_players_by_position
# from nflfunctions import sum_player_stats_per_season
from nflfunctions import sum_stats_per_grouping

import os
file_path = os.path.dirname(os.path.abspath(__file__))
play_duration_file = 'test.csv'
games_file = 'test2.csv'
play_duration_full_path = file_path + '\\' + play_duration_file
games_full_path = file_path + '\\' + games_file

play_duration_df = pd.read_csv(play_duration_full_path)
games_df = pd.read_csv(games_full_path)

# we only have data available for play duration past 2008 so
# subset the data appropriately
games_df = games_df[games_df["year"] >= 2009]

result_df = pd.merge(games_df, play_duration_df, left_on=['team', 'year'], right_on=['posteam', 'Year'])

print(play_duration_df.info())
print(games_df.info())

sacks_result_df = result_df['defense_sacks']
duration_result_df = result_df["PlayDuration"]

print(sacks_result_df.corr(duration_result_df))

_ = plt.plot(sacks_result_df, duration_result_df, linestyle='none', marker='.')
_ = plt.margins(0.02)
_ = plt.xlabel("sacks allowed per season")
_ = plt.ylabel("Play Duration (s)")

a, b = np.polyfit(sacks_result_df, duration_result_df, 1)
# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

_ = plt.plot(x, y)

plt.show()