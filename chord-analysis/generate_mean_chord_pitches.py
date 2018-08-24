import echo_nest_functions as enf

for i in range(0, 1301):
    try:
        dfs = enf.get_dfs_from_json("echonest_chords/" + str(i).zfill(4) + "/echonest.json")
        chord_timestamp_df = enf.get_chord_timestamp_df("echonest_chords/" + str(i).zfill(4) + "/full.lab", sep="\t")
        result_df = enf.get_df_with_pitch_class_cols(dfs, chord_timestamp_df)
        mean_pitch_df = enf.mean_pitch_squared_df(result_df)
        mean_pitch_df.to_csv("echonest_chords/" + str(i).zfill(4) + "/mean_chord_pitches.csv")
    except:
        print("echonest_chords/" + str(i).zfill(4) + "could not be found")


# enf.plot_adj_pitches_from_chord_df(mean_pitch_df, 'Chords and Pitch Classes to David Bowie\'s, "Space Oddity"')
