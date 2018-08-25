import pandas as pd
import echo_nest_functions as enf

df = pd.read_csv('chord_pitch_class_means.csv')
df_mean = enf.mean_pitch_squared_df(df)
print(df_mean.info())
df_mean_2 = df_mean[df_mean['chord'].str.contains(':maj$', regex=True)]  # regex match to only major chords
df_mean_3 = df_mean[df_mean['chord'].str.contains(':min$', regex=True)]  # regex match to only major chords
df_mean_4 = df_mean[df_mean['chord'].str.contains(':maj7$', regex=True)]  # regex match to only major chords
print(df_mean_2.info())
_ = enf.plot_adj_pitches_from_chord_df(df_mean_2, "Chords and Pitch Class Averages of Major Triads")
_ = enf.plot_adj_pitches_from_chord_df(df_mean_3, "Chords and Pitch Class Averages of Minor Triads")
_ = enf.plot_adj_pitches_from_chord_df(df_mean_4, "Chords and Pitch Class Averages of Maj 7 chords")
