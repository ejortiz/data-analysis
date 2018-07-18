import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

infection_df = pd.read_csv('Newman-SIR50-1mil-GS10-AD5-C04.csv')
infection_df['InfectionProbability'] = infection_df['InfRate'] / 10000  # add extra column with InfectionProbability
print(infection_df.tail())
