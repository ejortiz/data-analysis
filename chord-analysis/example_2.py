import echo_nest_functions
import numpy as np
import pandas as pd


def get_chord_from_timestamp_df(row, chord_timestamp_df):

    chords = chord_timestamp_df.loc[chord_timestamp_df.iloc[:, 0] <= row['start']]
    chords = chords.loc[chords.iloc[:, 1] >= row['start'] + row['duration']]
    if chords['chord'].size > 0:
        return chords['chord'].iloc[0]

# David bowie Space Oddity
dfs = echo_nest_functions.get_dfs_from_json("echonest_chords/0086/echonest.json")
chord_timestamp_df = pd.read_csv("echonest_chords/0086/full.lab", sep="\t")
# rename columns
chord_timestamp_df.columns = ['start_chord', 'end_chord', 'chord']

print(chord_timestamp_df.head())

segments_df = dfs['segments']

segments_df['chord'] = ''

segments_df['chord'] = segments_df.apply(get_chord_from_timestamp_df, axis=1, args=(chord_timestamp_df,))

segments_df.to_csv('test.csv')
