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

Output: Two bar plot. One csv file. The first one shows the supporting rate of input candiate for all the state in the US, in descending order. The second bar plot shows that the poverty rate of state. The state order is the same as the first one. [Analysis01_result01](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis01/Analysis01_result01)

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

The rest of the code generates the two bar plot using seaborn and result csv.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.41.08%20PM.png)


## [Analysis02](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/Analysis/Analysis02)

Input: 	State name for short

Output: Two pie plot. Two csv file. The first one shows the distribution of the education degree demography rate of the input state.
	The second one shows the racial demography distribution of the input state. [Analysis02_result01](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis02/Analysis02_result01), [Analysis02_result02](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis02/Analysis02_result02)
        
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


## [Analysis03](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/Analysis/Analysis03)

Input: 	State name for short

Output: One bar plot and one line plot. Two csv file. The bar plot shows the unemployment rate of the input state from 2007 to 2016.
	The line plot shows the supporting rate of two partys during the last three elections of the input state. [Analysis03_result01](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis03/Analysis03_result01), [Analysis04_result02](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis03/Analysis03_result02)
        
Description: This Analysis is trying to check whether their is a direct relation between the unemployment rate and the supporting rate 			of this two party.

note: This analysis merges two data source and make a new dataframe object

To do this analysis, run: 


    python Analysis03.py CA 

The out put would be shown as below:
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis03/Analysis03_img01.png)
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis03/Analysis03_img02.png)
    
Conclution: From plots above, there is no direct relation between the candiate supporting rate and the state unemployment rate.

###Deep into the code:

The first part of code as shown below, read the data and concat them together to make a new dataframe.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.49.41%20PM.png)

This code shown below collected the useful data from the original one. And then generate one new columns to represent the population of people of unemployment.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.50.16%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%206.51.26%20PM.png)

This code shown below sum up the data by state and use the total population and unemployment population calculate the unemployment rate 2016 for each state.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.09.21%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.10.27%20PM.png)

This code shown below generate a new columns which represent the supporting rate for input candidate and another columns which represent the state poverty rate. Then we sorted this result in descending order by the supporting rate.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.13.25%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.15.29%20PM.png)

This code shown below read the data from [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv) and merge it with the pre-existing aggregate dataframe by state.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.18.34%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.18.52%20PM.png)

This code shown below generate new dataframe based on unemployment rate from 07 to 15 which from the [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv) and unemployment rate of 16 from pre-exisiting dataframe.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.20.45%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.21.24%20PM.png)

The rest of the code generates the two plot using seaborn and the result csv.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.26.02%20PM.png)


## [Analysis04](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/Analysis/Analysis04)

Input: 	One year number from 2005 to 2014

Output: One bar plot. One csv file. The output bar plot shows the median household income for all state in US in the certain year. And shows the US average household income as a threshold line. csv [Analysis04_result01](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis04/Analysis04_result01)
        
Description: This Analysis is trying to show you the income condition for all the state in US, and tell you which one is lower than the 		US line and which one is higher.

note: This analysis concat a few data source and make a new dataframe object

To do this analysis, run: 


    python Analysis04.py 2013

The out put would be shown as below:
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/Analysis/Analysis04/Analysis04_img01.png)
    
Conclution: From plots above, you can see which state is rich and which one is not. It shows the US average level.

###Deep into the code:

The first part of code as shown below, read the data and concat them together to make a new dataframe.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.32.20%20PM.png)

This code shown below collected the useful data from the original one. And then generate one new columns to represent the year.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.37.52%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.38.46%20PM.png)

This code shown below aggregate the data by state calculate the average household income of each state, then merge them into one dataframe
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.43.16%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.43.36%20PM.png)

This code shown below get the median household income of the entire USA
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.44.58%20PM.png)

The rest of the code generates the bar plot using seaborn and the result csv.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%207.47.48%20PM.png)


## [Analysis05](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/Analysis/Analysis05)

Input: 	State name for short

Output: One state map. The map show you the unemployment rate of every county in this state.
        
Description: This Analysis is trying to show you the unemployment condition in certain state.

###note: This analysis use data visualization api bokeh

To do this analysis, run: 


    python Analysis05.py CA

The out put would be shown as below:
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%208.04.51%20PM.png)
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%208.05.13%20PM.png)
    ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%208.05.27%20PM.png)

###Deep into the code:

This code shown below import the bokeh api and import the counties data from bokeh.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%208.07.43%20PM.png)

This part of code as shown below, read the data and concat them together to make a new dataframe.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%208.13.30%20PM.png)

This code shown below is trying to match the unemployment rate with the position data from the bokeh according to the county.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%208.14.12%20PM.png)

The rest of the code generates the bar plot using seaborn.
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%208.16.45%20PM.png)
