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
print(infection_rate_summary_df.head())


# average the grouped infection
grouped_mean_df = infection_df.groupby(by=['InfectionProbability'])['NumInfected'].mean()
grouped_mean_df = grouped_mean_df.reset_index()  # reset the index of the dataframe
grouped_mean_df.columns = ['InfectionProb', 'NumInfectedMean']

# _ = plt.plot(grouped_mean_df['InfectionProb'], grouped_mean_df['NumInfectedMean'], linestyle='none', marker='.')
# _ = plt.show()
# print(grouped_df.head())
# print(grouped_mean_df.head())
