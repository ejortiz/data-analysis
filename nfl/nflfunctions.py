import numpy as np
import pandas as pd
import os

def get_all_players_by_position(dataframe, player_position):
    player_positions = dataframe['position']
    players_with_position = (player_positions == player_position)
    result = dataframe[players_with_position]
    return result

# def sum_player_stat_per_season(games_df, statistic_string)