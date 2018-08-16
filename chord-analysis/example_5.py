import echo_nest_functions
import ast
import pandas as pd
import matplotlib.pyplot as plt

# David bowie Space Oddity
dfs = echo_nest_functions.get_dfs_from_json("echonest_chords/0086/echonest.json")
chord_timestamp_df = pd.read_csv("echonest_chords/0086/full.lab", sep="\t")
# rename columns
chord_timestamp_df.columns = ['start_chord', 'end_chord', 'chord']

segments_df = dfs['segments']
segments_df['chord'] = ''
segments_df['chord'] = segments_df.apply(echo_nest_functions.get_chord_from_timestamp_df,
                                         axis=1, args=(chord_timestamp_df,))
segments_df['pitches'] = segments_df['pitches'].astype('str')

result_df = segments_df.apply(echo_nest_functions.extract_pitch_class_columns, axis=1)

c_major_df = result_df[result_df['chord'] == "C:maj"]
e_min_df = result_df[result_df['chord'] == "E:min"]

# grouped_df = result_df.groupby(by=['chord'])

echo_nest_functions.plot_pitches_from_chord_df(c_major_df)
echo_nest_functions.plot_pitches_from_chord_df(e_min_df)



