import json
from pandas.io.json import json_normalize


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






