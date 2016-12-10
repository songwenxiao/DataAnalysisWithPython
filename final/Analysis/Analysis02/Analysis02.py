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

education_df = us_election[['State','ST','Total.Population','At.Least.Bachelor.s.Degree','Less.Than.High.School']]
education_df['At.Least.Bachelor.s.Degree.Population'] = pd.Series(education_df['At.Least.Bachelor.s.Degree']*education_df['Total.Population']/100, index=education_df.index)
education_df['Less.Than.High.School.Population'] = pd.Series(education_df['Less.Than.High.School']*education_df['Total.Population']/100, index=education_df.index)

grouped_by_state = education_df[['State','Total.Population','At.Least.Bachelor.s.Degree.Population','Less.Than.High.School.Population']].groupby(education_df['ST']).sum()
grouped_by_state['High.School.Diploma.Population'] = pd.Series(grouped_by_state['Total.Population']-grouped_by_state['At.Least.Bachelor.s.Degree.Population']-grouped_by_state['Less.Than.High.School.Population'], index=grouped_by_state.index)

grouped_by_state['Highly.Education.Rate'] = pd.Series(grouped_by_state['At.Least.Bachelor.s.Degree.Population']/grouped_by_state['Total.Population'], index=grouped_by_state.index)
grouped_by_state['High.School.Education.Rate'] = pd.Series(grouped_by_state['High.School.Diploma.Population']/grouped_by_state['Total.Population'], index=grouped_by_state.index)
grouped_by_state['Less.High.School.Education.Rate'] = pd.Series(grouped_by_state['Less.Than.High.School.Population']/grouped_by_state['Total.Population'], index=grouped_by_state.index)
grouped_by_state.head(10)

grouped_by_state.iat[1,0]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('st', metavar='N', type=str, help='an integer for the accumulator')
args = parser.parse_args()

state = grouped_by_state.index == args.st
ceratin_state = grouped_by_state[state].iat[0,0]

# Data to plot
labels = 'At Least Bachelor Degree', 'High School Diploma', 'Less than High School'
sizes = [grouped_by_state[state].iat[0,4], grouped_by_state[state].iat[0,5], grouped_by_state[state].iat[0,6]]
colors = ['gold', 'yellowgreen', 'lightskyblue']
explode = (0.1, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title(args.st + "'s education distribution pie plot")
plt.savefig("Analysis02_img01.png")
plt.show()
plt.close()

race_df = us_election[['State','ST','Total.Population','White.not.Latino.Population','African.American.Population','Native.American.Population','Asian.American.Population','Latino.Population']]
race_df['White.not.Latino'] = pd.Series(race_df['White.not.Latino.Population']*race_df['Total.Population']/100, index=race_df.index)
race_df['African.American'] = pd.Series(race_df['African.American.Population']*race_df['Total.Population']/100, index=race_df.index)
race_df['Native.American'] = pd.Series(race_df['Native.American.Population']*race_df['Total.Population']/100, index=race_df.index)
race_df['Asian.American'] = pd.Series(race_df['Asian.American.Population']*race_df['Total.Population']/100, index=race_df.index)
race_df['Latino.Population'] = pd.Series(race_df['Latino.Population']*race_df['Total.Population']/100, index=race_df.index)

grouped_by_state_race = race_df[['State','Total.Population','White.not.Latino','African.American','Native.American','Asian.American','Latino.Population']].groupby(race_df['ST']).sum()

grouped_by_state_race['White.not.Latino.Rate'] = pd.Series(grouped_by_state_race['White.not.Latino']/grouped_by_state_race['Total.Population'], index=grouped_by_state_race.index)
grouped_by_state_race['African.American.Rate'] = pd.Series(grouped_by_state_race['African.American']/grouped_by_state_race['Total.Population'], index=grouped_by_state_race.index)
grouped_by_state_race['Native.American.Rate'] = pd.Series(grouped_by_state_race['Native.American']/grouped_by_state_race['Total.Population'], index=grouped_by_state_race.index)
grouped_by_state_race['Asian.American.Rate'] = pd.Series(grouped_by_state_race['Asian.American']/grouped_by_state_race['Total.Population'], index=grouped_by_state_race.index)
grouped_by_state_race['Latino.Population.Rate'] = pd.Series(grouped_by_state_race['Latino.Population']/grouped_by_state_race['Total.Population'], index=grouped_by_state_race.index)

# Data to plot
labels_race = 'White.not.Latino.Rate', 'African.American.Rate', 'Native.American.Rate', 'Asian.American.Rate', 'Latino.Population.Rate'
sizes_race = [grouped_by_state_race[state].iat[0,6], grouped_by_state_race[state].iat[0,7], grouped_by_state_race[state].iat[0,8],grouped_by_state_race[state].iat[0,9],grouped_by_state_race[state].iat[0,10]]
colors_race = ['gold', 'yellowgreen', 'lightskyblue','red','purple']
explode_race = (0.1, 0, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes_race, explode=explode_race, labels=labels_race, colors=colors_race,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title(args.st + "'s racial distribution pie plot")
plt.savefig("Analysis02_img02.png")
plt.show()