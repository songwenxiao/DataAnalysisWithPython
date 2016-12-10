import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot as plt
import argparse
#%matplotlib inline
est14 = pd.read_csv('../../data/est14ALL.csv',error_bad_lines=False,sep=',')
est13 = pd.read_csv('../../data/est13ALL.csv',error_bad_lines=False,sep=',')
est12 = pd.read_csv('../../data/est12ALL.csv',error_bad_lines=False,sep=',')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('st', metavar='N', type=str, help='an integer for the accumulator')
args = parser.parse_args()

est14 = est14[['Postal Code','Median Household Income']]
est14['time'] = pd.Series(2014, index=est14.index)
est14['Median Household Income'] = est14['Median Household Income'].astype(np.float64) 
est13 = est13[['Postal Code','Median Household Income']]
est13['time'] = pd.Series(2013, index=est13.index)
est13['Median Household Income'] = est13['Median Household Income'].astype(np.float64) 
est12 = est12[['Postal Code','Median Household Income']]
est12['time'] = pd.Series(2012, index=est13.index)
est12['Median Household Income'] = est12['Median Household Income'].astype(np.float64) 

est14_groupby = est14.groupby(est14['Postal Code'],as_index=True).mean()
est13_groupby = est13.groupby(est13['Postal Code'],as_index=True).mean()
est12_groupby = est12.groupby(est13['Postal Code'],as_index=True).mean()

frames = [est14_groupby, est13_groupby, est12_groupby]

result = pd.concat(frames)

year = int(args.st)
sub_result = result.loc[result['time'] == year]
median = sub_result.iat[-8,0]
print(median)
result_without_us = sub_result.drop(['US'])

result_final = result_without_us.reset_index()
fig, ax = plt.subplots()
# the size of A4 paper
fig.set_size_inches(14.7, 8.27)
ax = sns.barplot(x='Postal Code',y='Median Household Income',data=result_final,color='#3778bf',ax=ax)
plt.axhline(y=median,color='#3778bf',ls='dashed')
plt.title('State Median Household Income in year ' + args.st)
plt.savefig("Analysis04_img01.png")