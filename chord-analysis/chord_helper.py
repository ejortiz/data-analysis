class ChordHelper:

    chord_names_list = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

    @staticmethod
    def add_note_number_cols_to_df(chord_df):
        modded_chord_df = chord_df
        modded_chord_df['note_0'] = ''
        modded_chord_df['note_1'] = ''
        modded_chord_df['note_2'] = ''
        modded_chord_df['note_3'] = ''
        modded_chord_df['note_4'] = ''
        modded_chord_df['note_5'] = ''
        modded_chord_df['note_6'] = ''
        modded_chord_df['note_7'] = ''
        modded_chord_df['note_8'] = ''
        modded_chord_df['note_9'] = ''
        modded_chord_df['note_10'] = ''
        modded_chord_df['note_11'] = ''

        return modded_chord_df

    def get_chord_from_timestamp(self, row):
        chord_name = row['chord']
        chords = chords.loc[chords.iloc[:, 1] >= row['start'] + row['duration']]
        if chords['chord'].size > 0:
            return chords['chord'].iloc[0]
