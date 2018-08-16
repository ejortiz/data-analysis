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


# grouped_df = result_df.groupby(by=['chord'])

# grouped_df.plot(y=['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'])
# c_major_df.plot(y=['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'], kind='bar')

ax = c_major_df.plot(y='C', kind='bar')
c_major_df.plot(y='C#/Db', ax=ax, color='orange', kind='bar')
c_major_df.plot(y='D', ax=ax, color='yellow', kind='bar')
c_major_df.plot(y='D#/Eb', ax=ax, color='green', kind='bar')
c_major_df.plot(y='E', ax=ax, color='blue', kind='bar')
c_major_df.plot(y='F', ax=ax, color='purple', kind='bar')
c_major_df.plot(y='F#/Gb', ax=ax, color='gray', kind='bar')
c_major_df.plot(y='G', ax=ax, color='black', kind='bar')
c_major_df.plot(y='G#/Ab', ax=ax, color='turquoise', kind='bar')
c_major_df.plot(y='A', ax=ax, color='maroon', kind='bar')
c_major_df.plot(y='A#/Bb', ax=ax, color='silver', kind='bar')
c_major_df.plot(y='B', ax=ax, color='pink', kind='bar')
plt.show()
print(c_major_df.head())

