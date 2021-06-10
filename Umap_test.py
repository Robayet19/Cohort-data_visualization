import numpy as np
import os
import umap
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

main_directory = os.getcwd()
new_directory = 'C:\\Users\\rmchowdh\Dropbox (ASU)\\Programs and Data for Team\\Programs\\NN results with proteome projection_NIBIB and DHS\\Programs used for the project\\Data_Wafer_187'
temp_directory = os.chdir(new_directory)
# filename
filename1 = 'sequence_data_NIBIB_ND_187_CTS_CV3_19-Apr-2021-17-34.csv'
filename2 = 'sequence_data_NIBIB_HBV_187_CTS_CV3_20-Apr-2021-14-42.csv'
filename3 = 'sequence_data_NIBIB_HCV_187_CTS_CV3_20-Apr-2021-14-40.csv'
filename4 = 'sequence_data_NIBIB_WNV_187_CTS_CV3_20-Apr-2021-14-47.csv'
# read the datasets
sequence_data1 = pd.read_csv(filename1, header=None)
data1 = sequence_data1.iloc[:, 1:]
sequence_data2 = pd.read_csv(filename2, header=None)
data2 = sequence_data2.iloc[:, 1:]
sequence_data3 = pd.read_csv(filename3, header=None)
data3 = sequence_data3.iloc[:, 1:]
sequence_data4 = pd.read_csv(filename4, header=None)
data4 = sequence_data4.iloc[:, 1:]

# combine the datasets
data = np.concatenate([data1, data2, data3, data4], axis=1)
data = pd.DataFrame(data)
data = data.T  # reverse the array to add sample names later. This is required to reduce features (peptides)

# label each column with the corresponding cohort name
cohorts = ['ND', 'HBV', 'HCV', 'WNV']
num_sample_cohort = [data1.shape[1], data2.shape[1], data3.shape[1], data4.shape[1]]
sample_ND = ["ND"] * num_sample_cohort[0]
sample_HBV = ["HBV"] * num_sample_cohort[1]
sample_HCV = ["HCV"] * num_sample_cohort[2]
sample_WNV = ["WNV"] * num_sample_cohort[3]
sample_name = sample_ND + sample_HBV + sample_HCV + sample_WNV
sample_name = pd.Series(sample_name)  # convert to panda Series type

# apply umap
reducer = umap.UMAP(random_state=42)
reducer.fit(data)
embedding = reducer.fit_transform(data)
embedding.shape
## plot the reduced data
# color_cohort = [sns.color_palette()[x] for x in sample_name.map({"ND": 'g', "HBV": 'r', "HCV": 'b', "WNV": 'k'})]
fig1, ax = plt.subplots()
color_cohort = {"ND": 'g', "HBV": 'r', "HCV": 'b', "WNV": 'k'}
for i in cohorts:
    ii = np.where(sample_name == i)
    ax.scatter(embedding[ii, 0], embedding[ii, 1], c=color_cohort[i], label=i, s=15)
ax.legend()
plt.title('UMAP projection of the ND_HBV_HCV_WNV dataset', fontsize=24)
plt.show()
