import numpy as np
import pandas as pd
import os

def get_all_players_by_position(dataframe, player_position):
    player_positions = dataframe['position']
    players_with_position = (player_positions == player_position)
    result = dataframe[players_with_position]
    return result

def sum_player_stats_per_season(games_df, stats_list):
    return games_df.groupby(by=['player_id', 'year', 'team'])[stats_list].sum()

def sum_stats_per_grouping(games_df, stats_to_group_by, stats_to_sum, reset_index=True):
    result_df = games_df.groupby(by=stats_to_group_by)[stats_to_sum].sum()
    if(reset_index):
       result_df = result_df.reset_index()
    return result_df