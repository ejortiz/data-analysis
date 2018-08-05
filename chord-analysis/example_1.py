import numpy as np
import librosa
import pandas as pd
import json
from pandas.io.json import json_normalize
# song 86: "Space Oddity" by David Bowie

with open('echonest_chords/0086/echonest.json', 'r') as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

meta_df = json_normalize(json_data['meta'])
track_df = json_normalize(json_data['track'])
bars_df = json_normalize(json_data['bars'])
beats_df = json_normalize(json_data['beats'])
tatums_df = json_normalize(json_data['tatums'])
sections_df = json_normalize(json_data['sections'])
segments_df = json_normalize(json_data['segments'])

print(segments_df.head())
