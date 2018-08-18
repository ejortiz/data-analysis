import json
import ast
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

chord_names_list = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']


def get_chord_timestamp_df(full_lab_filepath, sep="\t"):
    df = pd.read_csv(full_lab_filepath, sep=sep)
    df.columns = ['start_chord', 'end_chord', 'chord']  # Rename columns
    return df


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


def get_chord_from_timestamp(row, chord_timestamp_df):

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


def get_df_with_pitch_class_cols(echonest_data_df, chord_timestamp_df):
    segments_df = echonest_data_df['segments']
    segments_df['chord'] = ''
    segments_df['chord'] = segments_df.apply(get_chord_from_timestamp,
                                             axis=1, args=(chord_timestamp_df,))
    segments_df['pitches'] = segments_df['pitches'].astype('str')

    result_df = segments_df.apply(extract_pitch_class_columns, axis=1)
    return result_df


def mean_pitch_val_df(chord_and_pitch_segment_df):
    grouped_df = chord_and_pitch_segment_df.groupby(by=['chord'])
    mean_pitch_df = grouped_df[
        'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'].mean()
    mean_pitch_df = mean_pitch_df.reset_index()
    return mean_pitch_df


def mean_pitch_squared_df(chord_and_pitch_segment_df):
    grouped_df = chord_and_pitch_segment_df.groupby(by=['chord'])
    mean_pitch_df = grouped_df[
        'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'].mean()
    mean_pitch_df = mean_pitch_df.reset_index()
    mean_pitch_squared = mean_pitch_df.drop(columns=['chord'])
    print(mean_pitch_df.info())
    mean_pitch_squared = mean_pitch_squared.apply(lambda x: x*x)
    mean_pitch_squared.insert(0, 'chord', mean_pitch_df['chord'])

    return mean_pitch_squared


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


def plot_adj_pitches_from_chord_df(chord_df, graph_title):
    chord_df.plot(x='chord', y=['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'],
                  kind='bar')
    plt.title(graph_title)
    plt.show()

