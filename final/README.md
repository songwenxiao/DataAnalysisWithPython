# Wenxiao Song final project

## Introduction

This final project contains five analysis. The first two analysis are trying to check that whether the supporting rate of Democrat and Republican has something to do with poverty rate or unemployment rate. The third one is trying to show that the median household income of all the state in the US. The last two analysis are trying to show some information about the certain state.

## Data Source description

The data source contains in 15 csv files. [Link to the data source](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/data). 
The first, forth and fifth analysis are based on [xaa.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xaa.csv), [xab.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xab.csv), [xac.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xac.csv) and [xad.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xad.csv). 
The second analysis are based on all the csv file.
The third analysis are based on [xaa.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xaa.csv), [xab.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xab.csv), [xac.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xac.csv), [xad.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xad.csv) and [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv)

The [xaa.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xaa.csv), [xab.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xab.csv), [xac.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xac.csv) and [xad.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xad.csv) are splited from one data file [usa-2016-presidential-election-by-county.csv](https://public.opendatasoft.com/explore/dataset/usa-2016-presidential-election-by-county/table/). They have the same columns.
The columns of these files are covered from state, county, votes, race ratio, poverty rate, business structure to age distriubtion. 
The sample data are shown below:

![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.03.12%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.03.41%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.04.12%20PM.png)

The [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv) contains some useful informations like state, unemployment rate from 2007 to 2015. 

The sample data of [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv) are shown below:

![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.17.38%20PM.png)

The [est05All.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/est05ALL.csv) to [est14All.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/est14ALL.csv) contains information like state, county, median househould income.

The sample data of [est05All.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/est05ALL.csv) are shown below:

![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.38.04%20PM.png) ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.38.19%20PM.png)

###Since all five analysis covers so many columns and they are so different from each other, I decide to put the collected data process into seperate analysis file. I will explain later in each analysis. 


## [Analysis01](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/Analysis/Analysis01)

Input: 	Candidate Last Name(Trump or Hillary)

Output: Two bar plot. The first one shows the supporting rate of input candiate for all the state in the US, in descending order. The 			second bar plot shows that the poverty rate of state. The state order is the same as the first one.

Description: This analysis is trying to check whether their is a direct relation between the candiate supporting rate and the state 			poverty rate.

To do this analysis, run: 

    python Analysis01.py Hillary 
    
The out put would be shown as below:
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Analysis01_img01.png)
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Analysis01_img02.png)
    
Conclution: From plots above, there is no direct relation between the candiate supporting rate and the state poverty rate.

###Deep into the code:

The first part of code as shown below, read the data and concat them together to make a new dataframe.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.44.15%20PM.png)

This code shown below collected the useful data from the original one.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.22.35%20PM.png)

This code shown below generate a new columns called 'Total.Population.Under.Poverty.Line'. It represent the total number of population under the poverty rate for each county. Then we sum up the total number of total population, votes, population under poverty according to the state. We will get the total number of population, votes, total number of people under poverty for every state.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.30.33%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.30.48%20PM.png)

This code shown below generate a new columns which represent the supporting rate for input candidate and another columns which represent the state poverty rate. Then we sorted this result in descending order by the supporting rate.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.38.09%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.40.46%20PM.png)

The rest of the code generates the two bar plot using seaborn.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.41.08%20PM.png)


## [Analysis02](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/Analysis/Analysis02)

Input: 	State name for short

Output: Two pie plot. The first one shows the distribution of the education degree demography rate of the input state.
		The second one shows the racial demography distribution of the input state.
        
Description: This Analysis is trying to show you this two demography information of the certain state.

To do this analysis, run: 


    python Analysis02.py CA 

The out put would be shown as below:
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis02/Analysis02_img01.png)
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis02/Analysis02_img02.png)
    
Conclution: From plots above, it will show you the demography information and education situation of certain state.

###Deep into the code:

The first part of code as shown below, read the data and concat them together to make a new dataframe.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.49.41%20PM.png)

This code shown below collected the useful data from the original one. And then generate two new columns to represent the population of people less than high school diploma and people at least bachelor degree.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.50.16%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.51.26%20PM.png)

This code shown below sum up the data by state and use the total population and population less than high school diploma and population at least bachelor degree to calculation the population for high school diploma.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.30.33%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.30.48%20PM.png)

This code shown below generate a new columns which represent the supporting rate for input candidate and another columns which represent the state poverty rate. Then we sorted this result in descending order by the supporting rate.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.54.03%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.54.14%20PM.png)

The rest of the code generates the two bar plot using seaborn.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.00.22%20PM.png)

The racial distribution code actually is using the same approach.
