import pandas as pd
import numpy as np
import seaborn as sns
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

st = ""
if args.st == 'Trump':
	st = 'Trump D'
elif args.st == 'Hillary':
	st = 'Clinton H'

candidate_df = us_election[['State','ST',st,'votes','Total.Population','Poverty.Rate.below.federal.poverty.threshold']]


candidate_df['Total.Population.Under.Poverty.Line'] = pd.Series(candidate_df['Poverty.Rate.below.federal.poverty.threshold']*candidate_df['Total.Population']/100, index=candidate_df.index)
grouped_by_state = candidate_df[['State',st,'votes','Total.Population','Total.Population.Under.Poverty.Line']].groupby(candidate_df['ST']).sum()

grouped_by_state['e'] = pd.Series(grouped_by_state[st]/grouped_by_state['votes'], index=grouped_by_state.index)
grouped_by_state['State.Poverty.Rate'] = pd.Series(grouped_by_state['Total.Population.Under.Poverty.Line']/grouped_by_state['Total.Population'], index=grouped_by_state.index)
grouped_by_state.sort(['e'], ascending=[False], inplace=True)

candidates_votes = grouped_by_state.reset_index()
fig, ax = plt.subplots()
# the size of A4 paper
fig.set_size_inches(14.7, 8.27)
ax = sns.barplot(x='ST',y='e',data=candidates_votes,color='#3778bf',ax=ax)
plt.title(st + "'s supporting rate (Ascending order)")
plt.savefig("Analysis01_img01.png")
plt.close()

candidates_votes = grouped_by_state.reset_index()
fig2, ax2 = plt.subplots()
# the size of A4 paper
fig2.set_size_inches(14.7, 8.27)
ax2 = sns.barplot(x='ST',y='State.Poverty.Rate',data=candidates_votes,color='#3778bf',ax=ax2)
plt.title("State Poverty Rate Barplot 2016")
plt.savefig("Analysis01_img02.png")
candidates_votes.to_csv('Analysis01_result01', sep='\t', encoding='utf-8')