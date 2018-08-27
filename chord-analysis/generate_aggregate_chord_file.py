import echo_nest_functions as enf
import pandas as pd

df = pd.DataFrame()
for i in range(0, 1301):
    try:
        dfs = enf.get_dfs_from_json("echonest_chords/" + str(i).zfill(4) + "/echonest.json")
        chord_timestamp_df = enf.get_chord_timestamp_df("echonest_chords/" + str(i).zfill(4) + "/full.lab", sep="\t")
        song_df = enf.get_df_with_pitch_class_cols(dfs, chord_timestamp_df)
        song_df.insert(0, 'track_number', value=str(i).zfill(4))
        df = df.append(song_df, ignore_index=True)
    except:
        print("echonest_chords/" + str(i).zfill(4) + "could not be found")

df.to_csv('total_chord_pitches.csv')
