import numpy as np
import os
import seaborn as sns
import pandas as pd

Mednorm = True  # turn it true for median normalizes data

main_directory = os.getcwd()
new_directory = 'C:\\Users\\rmchowdh\\Dropbox (ASU)\\Programs and Data for Team\\Programs\\NN results with proteome ' \
                'projection_NIBIB and DHS\\Data\\Data_CV3 '
os.chdir(new_directory)
# Now read the binding data in each of the six cohorts
if Mednorm:
    filename1 = 'sequence_data_NIBIB_Dengue_ML_CTSSeraCare_mod_CV317-Jul-2020-00-08.csv'
    filename2 = 'sequence_data_NIBIB_WNV_ML_mod_CV315-Jul-2020-23-57.csv'
    filename3 = 'sequence_data_NIBIB_HCV_ML_mod_CV317-Jul-2020-16-50.csv'
    filename4 = 'sequence_data_NIBIB_HBV_ML_mod_CV316-Jul-2020-00-01.csv'
    filename5 = 'sequence_data_NIBIB_Chagas_ML_mod_CV316-Jul-2020-00-02.csv'
    filename6 = 'sequence_data_NIBIB_Normal_ML_mod_CV315-Jul-2020-23-50.csv'
else:
    filename1 = 'sequence_data_NIBIB_Dengue_ML_CTSSeraCare_mod_CV317-Jul-2020-00-08.csv'
    filename2 = 'sequence_data_NIBIB_WNV_ML_noMed_CV315-Jul-2020-23-16.csv'
    filename3 = 'sequence_data_NIBIB_HCV_ML_noMed_CV3_17-Jul-2020-16-56.csv'
    filename4 = 'sequence_data_NIBIB_HBV_ML_noMed_CV315-Jul-2020-23-25.csv'
    filename5 = 'sequence_data_NIBIB_Chagas_ML_mod_CV316-Jul-2020-00-02.csv'
    filename6 = 'sequence_data_NIBIB_Normal_ML_noMed_CV315-Jul-2020-23-35.csv'

# read the datasets and take the average data for each cohort
seq_data1 = pd.read_csv(filename1, header=None)
data1_mean = pd.DataFrame(np.mean(seq_data1.iloc[:, 1:], axis=1))
seq_data2 = pd.read_csv(filename2, header=None)
data2_mean = pd.DataFrame(np.mean(seq_data2.iloc[:, 1:], axis=1))
seq_data3 = pd.read_csv(filename3, header=None)
data3_mean = pd.DataFrame(np.mean(seq_data3.iloc[:, 1:], axis=1))
seq_data4 = pd.read_csv(filename4, header=None)
data4_mean = pd.DataFrame(np.mean(seq_data4.iloc[:, 1:], axis=1))
seq_data5 = pd.read_csv(filename5, header=None)
data5_mean = pd.DataFrame(np.mean(seq_data5.iloc[:, 1:], axis=1))
seq_data6 = pd.read_csv(filename6, header=None)
data6_mean = pd.DataFrame(np.mean(seq_data6.iloc[:, 1:], axis=1))

# combine six cohort average data
# data = pd.Series(np.concatenate([data1_mean, data2_mean, data3_mean, data4_mean, data5_mean, data6_mean]))
data = np.concatenate([data1_mean, data2_mean, data3_mean, data4_mean, data5_mean, data6_mean], axis=1)
cohorts = ['DENV4', 'WNV', 'HCV', 'HBV', 'Chagas', 'Uninfected']

# plot the data using violinplot
ax = sns.violinplot(data=np.log10(data), inner='box')
ax.set_xticklabels(cohorts)
ax.set(xlabel='Cohort', ylabel='Log10 Intensity')
ax.set_title('Distribution of serum IgG binding in six cohorts', fontsize=16)

