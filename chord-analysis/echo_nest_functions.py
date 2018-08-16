import json
import ast
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt



def get_dfs_from_json(json_file_path):

    with open(json_file_path, 'r') as json_data:
        json_result = json.load(json_data)

    result = dict()
    meta_df = json_normalize(json_result['meta'])
    track_df = json_normalize(json_result['track'])
    bars_df = json_normalize(json_result['bars'])
    beats_df = json_normalize(json_result['beats'])
    tatums_df = json_normalize(json_result['tatums'])
    sections_df = json_normalize(json_result['sections'])
    segments_df = json_normalize(json_result['segments'])

    result["meta"] = meta_df
    result["track"] = track_df
    result["bars"] = bars_df
    result["beats"] = beats_df
    result["tatums"] = tatums_df
    result["sections"] = sections_df
    result["segments"] = segments_df

    return result


def get_chord_from_timestamp_df(row, chord_timestamp_df):

    chords = chord_timestamp_df.loc[chord_timestamp_df.iloc[:, 0] <= row['start']]
    chords = chords.loc[chords.iloc[:, 1] >= row['start'] + row['duration']]
    if chords['chord'].size > 0:
        return chords['chord'].iloc[0]


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


def plot_pitches_from_chord_df(chord_df):
    ax = chord_df.plot(y='C', kind='bar')
    chord_df.plot(y='C#/Db', ax=ax, color='orange', kind='bar')
    chord_df.plot(y='D', ax=ax, color='yellow', kind='bar')
    chord_df.plot(y='D#/Eb', ax=ax, color='green', kind='bar')
    chord_df.plot(y='E', ax=ax, color='blue', kind='bar')
    chord_df.plot(y='F', ax=ax, color='purple', kind='bar')
    chord_df.plot(y='F#/Gb', ax=ax, color='gray', kind='bar')
    chord_df.plot(y='G', ax=ax, color='black', kind='bar')
    chord_df.plot(y='G#/Ab', ax=ax, color='turquoise', kind='bar')
    chord_df.plot(y='A', ax=ax, color='maroon', kind='bar')
    chord_df.plot(y='A#/Bb', ax=ax, color='silver', kind='bar')
    chord_df.plot(y='B', ax=ax, color='pink', kind='bar')
    plt.show()
    return

