import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

file_path = os.path.dirname(os.path.abspath(__file__))
nfl_pbp_file = 'nfl-pbp-2009-2017-v4.csv'
dir_path = file_path + '\\nfl-play-by-play'
full_path = dir_path + "\\" + nfl_pbp_file

pbp_df = pd.read_csv(full_path, low_memory=False)

# add "Play duration" and "LastPassOutCome" column to the df
pbp_df["PlayDuration"] = pbp_df.groupby("GameID")["PlayTimeDiff"].shift(-1)
pbp_df["LastPlayPassOutcome"] = pbp_df.groupby("GameID")["PassOutcome"].shift(1)

print(pbp_df.head())

'''
Finding oddities for play time
https://sports.yahoo.com/one-longest-plays-nfl-history-bucs-unleash-chaos-210654158.html
according to this yahoo article, this bucs play has to be among one of the longest in nfl history at 45 seconds
so let's subset our dataframe
'''

'''
Remember that on the running game, the clock is still winding down, so our real metric are 
'''
pbp_df = pbp_df[(pbp_df["PlayDuration"] < 45) & (pbp_df["PassOutcome"] == 'Incomplete Pass') &
                (pbp_df["LastPlayPassOutcome"] == 'Incomplete Pass')]


mean_play_time = pbp_df["PlayDuration"].mean()
std_dev_play_time = pbp_df["PlayDuration"].std()
median_play_time = pbp_df["PlayDuration"].median()


print("Mean Play Time: " + str(mean_play_time))
print("Std Dev Play Time: " + str(std_dev_play_time))
print("Median Play Time: " + str(median_play_time))

sns.boxplot(y=pbp_df["PlayDuration"])
plt.ylabel("Play Duration (s)")
plt.title("Play Duration for Second-Straight Incomplete Pass")
plt.show()
