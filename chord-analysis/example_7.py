import echo_nest_functions as enf
# David bowie Space Oddity
dfs = enf.get_dfs_from_json("echonest_chords/0086/echonest.json")
chord_timestamp_df = enf.get_chord_timestamp_df("echonest_chords/0086/full.lab", sep="\t")

result_df = enf.get_df_with_pitch_class_cols(dfs, chord_timestamp_df)
mean_pitch_df = enf.mean_pitch_squared_df(result_df)

enf.plot_adj_pitches_from_chord_df(mean_pitch_df, 'Chords and Pitch Classes to David Bowie\'s, "Space Oddity"')
