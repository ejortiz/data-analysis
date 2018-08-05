import echo_nest_functions
import numpy as np
import pandas as pd

# David bowie Space Oddity
dfs = echo_nest_functions.get_dfs_from_json("echonest_chords/0086/echonest.json")

print(dfs['segments'].head())
