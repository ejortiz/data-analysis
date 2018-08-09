import echo_nest_functions
import ast
import pandas as pd

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

print(segments_df.info())
def extract_pitch_class_columns(row):

    # list of pitches extracted from the pitch column of the dataframe
    pitches = ast.literal_eval(row['pitches'])
    row['C'] = pitches[0]
    row['C#/Db'] = pitches[1]
    row['D'] = pitches[2]
    row['D#/Eb'] = pitches[3]
    row['E'] = pitches[4]
    row['F'] = pitches[5]
    row['F#/Gb'] = pitches[6]
    row['G'] = pitches[7]
    row['G#/Ab'] = pitches[8]
    row['A'] = pitches[9]
    row['A#/Bb'] = pitches[10]
    row['B'] = pitches[11]
    return row

result_df = segments_df.apply(extract_pitch_class_columns, axis=1)

result_df.to_csv('test_from_example_3.csv')

print(result_df.head())
