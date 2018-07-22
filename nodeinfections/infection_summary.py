import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

infection_df = pd.read_csv('Newman-SIR50-1mil-GS10-AD5-C04.csv')
infection_df['InfectionProbability'] = infection_df['InfRate'] / 10000  # add extra column with InfectionProbability

grouped_df = infection_df.groupby(by=['InfRate'])  # group the df by infection rate

infection_rate_summary_init = {'mean': grouped_df['NumInfected'].mean(), 'quartile-1': grouped_df['NumInfected'].quantile(.25),
                             'median': grouped_df['NumInfected'].quantile(.5),
                             'quartile-3': grouped_df['NumInfected'].quantile(.75),
                             'min': grouped_df['NumInfected'].min(),
                             'max': grouped_df['NumInfected'].max(),
                             'lower-outlier-bound': grouped_df['NumInfected'].quantile(.25) -
                                                    ((grouped_df['NumInfected'].quantile(.75) -
                                                      grouped_df['NumInfected'].quantile(.25)) * 1.5),
                             'upper-outlier-bound': grouped_df['NumInfected'].quantile(.75) +
                                                    ((grouped_df['NumInfected'].quantile(.75) -
                                                      grouped_df['NumInfected'].quantile(.25)) * 1.5)
                             }
infection_rate_summary_df = pd.DataFrame(data=infection_rate_summary_init)

# reset the index of the infection rates so we can do a join with the existing infection df
infection_rate_stats = infection_rate_summary_df.reset_index()

# Do a join on the on the infection rates columns
aggregate_df = pd.merge(infection_df, infection_rate_stats, left_on=['InfRate'], right_on=['InfRate'])
aggregate_df['outlier'] = (aggregate_df['NumInfected'] > aggregate_df['upper-outlier-bound']) | \
                          (aggregate_df['NumInfected'] < aggregate_df['lower-outlier-bound'])

aggregate_df.to_csv('node-infection-stats.csv')
print(aggregate_df.head())

