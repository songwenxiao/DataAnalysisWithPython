import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot as plt
import argparse
#%matplotlib inline
us_election1 = pd.read_csv('../../data/xaa.csv',error_bad_lines=False,sep=';')
us_election2 = pd.read_csv('../../data/xab.csv',error_bad_lines=False,sep=';')
us_election3 = pd.read_csv('../../data/xac.csv',error_bad_lines=False,sep=';')
us_election4 = pd.read_csv('../../data/xad.csv',error_bad_lines=False,sep=';')
frames = [us_election1, us_election2, us_election3, us_election4]

us_election = pd.concat(frames)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('st', metavar='N', type=str, help='an integer for the accumulator')
args = parser.parse_args()

election_us = us_election[['State','ST','Trump D','Clinton H','votes','Republicans 12','Democrats 12','Total 12','Democrats 08','Republicans 08','Total 08','Unemployment','Total.Population']]

election_us['Unployment_Population'] = pd.Series(election_us['Unemployment']*election_us['Total.Population'], index=election_us.index)

grouped_by_state = election_us[['ST','State','Trump D','Clinton H','votes','Republicans 12','Democrats 12','Total 12','Democrats 08','Republicans 08','Total 08','Unployment_Population','Total.Population']].groupby(election_us['ST'],as_index=True).sum()
grouped_by_state['Unemployment_rate_2016'] = pd.Series(grouped_by_state['Unployment_Population']/grouped_by_state['Total.Population'], index=grouped_by_state.index)
grouped_by_state2 = grouped_by_state.reset_index()

grouped_by_state2['Democrats.Rate.16'] = pd.Series(grouped_by_state2['Clinton H']/grouped_by_state2['votes'], index=grouped_by_state2.index)
grouped_by_state2['Republican.Rate.16'] = pd.Series(grouped_by_state2['Trump D']/grouped_by_state2['votes'], index=grouped_by_state2.index)
grouped_by_state2['Republican.Rate.12'] = pd.Series(grouped_by_state2['Republicans 12']/grouped_by_state2['Total 12'], index=grouped_by_state2.index)
grouped_by_state2['Democrats.Rate.12'] = pd.Series(grouped_by_state2['Democrats 12']/grouped_by_state2['Total 12'], index=grouped_by_state2.index)
grouped_by_state2['Democrats.Rate.08'] = pd.Series(grouped_by_state2['Democrats 08']/grouped_by_state2['Total 08'], index=grouped_by_state2.index)
grouped_by_state2['Republican.Rate.08'] = pd.Series(grouped_by_state2['Republicans 08']/grouped_by_state2['Total 08'], index=grouped_by_state2.index)

unemployment_us = pd.read_csv('../../data/Unemployment.csv',error_bad_lines=False,sep=',')

unemployment_us1 = unemployment_us[['State','Unemployment_rate_2007','Unemployment_rate_2008','Unemployment_rate_2009','Unemployment_rate_2010','Unemployment_rate_2011','Unemployment_rate_2012','Unemployment_rate_2013','Unemployment_rate_2014','Unemployment_rate_2015']]

merge_us = pd.merge(grouped_by_state2, unemployment_us1, left_on='ST', right_on='State')

state = merge_us['ST'] == args.st
certain_state = merge_us[state]

certain_st = {'ST':[certain_state.iat[0,0], certain_state.iat[0,0], certain_state.iat[0,0], certain_state.iat[0,0], certain_state.iat[0,0], certain_state.iat[0,0],certain_state.iat[0,0],certain_state.iat[0,0],certain_state.iat[0,0],certain_state.iat[0,0]], 
     'time':[2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
     'Unemployment_Rate':[certain_state.iat[0,-9]/100,certain_state.iat[0,-8]/100,certain_state.iat[0,-7]/100,certain_state.iat[0,-6]/100,certain_state.iat[0,-5]/100,certain_state.iat[0,-4]/100,certain_state.iat[0,-3]/100,certain_state.iat[0,-2]/100,certain_state.iat[0,-1]/100,certain_state.iat[0,12]]}
result_unemployment = pd.DataFrame(certain_st)

ax = sns.pointplot(x="time", y="Unemployment_Rate",
                    data=result_unemployment,
                    markers=["o", "x"],
                    linestyles=["-", "--"])
plt.title(args.st + "'s unemployment rate from 2007-2016")
plt.savefig("Analysis03_img01.png")
plt.close()

certain_st2 = {'ST':[certain_state.iat[0,0], certain_state.iat[0,0], certain_state.iat[0,0],certain_state.iat[0,0], certain_state.iat[0,0], certain_state.iat[0,0]],
     'time':[2008, 2012, 2016,2008, 2012, 2016],
     'Supporting_Rate':[certain_state.iat[0,17],certain_state.iat[0,16],certain_state.iat[0,13],certain_state.iat[0,18],certain_state.iat[0,15],certain_state.iat[0,14]],
     'Supporting_party':['Democrat','Democrat','Democrat','Republican','Republican','Republican']}
result_support = pd.DataFrame(certain_st2)

ax2 = sns.pointplot(x="time", y="Supporting_Rate",hue='Supporting_party',
                    data=result_support,
                    markers=["o", "x"],
                    linestyles=["-", "--"])
plt.title("Two party's supporting rate in " + args.st + " for the past three elections")
plt.savefig("Analysis03_img02.png")