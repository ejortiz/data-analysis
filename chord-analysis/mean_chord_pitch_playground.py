import echo_nest_functions as enf
import pandas as pd
df = pd.DataFrame()
for i in range(0, 1301):
    try:
        song_df = pd.read_csv("echonest_chords/" + str(i).zfill(4) + "/mean_chord_pitches.csv")
        song_df.insert(0, 'track_number', value=str(i).zfill(4))
        df = df.append(song_df, ignore_index=True)
    except:
        print("echonest_chords/" + str(i).zfill(4) + "could not be found")

print(df.tail())
df.to_csv("chord_pitch_class_means.csv")
