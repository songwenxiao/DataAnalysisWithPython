# DataAnalysisPython
Repository Contains material for subject - "Data Analysis using Python" Fall 2016

Assignemnt 2:
The dataCollector is resposible for  collecting data. You can input what ever you want here. I strongly recommand you search trump and hillary, since the dataAnalyzer can only analyze these two word.
The dataAnalyzer is responisble for analyze the data collected by the dataCollector. 
You can enter "friend", which can caculate the average friends that poster has. 
You can enter "location", which can help you to get the which state post Trump the most and which state post Hillary the most.
You can enter "retweet" so that you can get the top 10 tweets which gets the most retweet time.
You can enter "influential" so that you can get the most influential tweet.
You can enter "time" so that you can get the most post day.

Midterm:
Analysis1: Using request module and stackoverflow api, search for 100 questions that has the python tag. Then using questions id to search for their owner's profile. Get the top 10 reputation user and store them in a json file.

Analysis2: Open the json file that stored in Analysis1, using the top 10 owner's id to send request to get their badges count and then caculate the weightadge and sort. Find out which one has the highest weightadge.

Analysis3: Using request module and stackoverflow api, search for 100 users that has the questions about python, use their id to get user profile to find out whether they have badge. Caculate how many user among 100 users have badges. Using the badges' name to send request to find out the award count. Find out the top 10 popular badges among users.

Analysis4: Send request to get all questions posted on 10/29/2016, caculate the average answer times among these questions. Meanwhile, send request using tag name to find out how many times do these tags be used.

Analysis5: Open the json file that stored in Analysis1, using owner's id to find out their favorite questions, find out the top 10 score questions among these  questions.

Final Project:
Analysis01: \n
Input: 	Candidate Last Name(Trump or Hillary)
Output: Two bar plot. The first one shows the supporting rate of input candiate for all the state in the US, in descending order. The 			second bar plot shows that the poverty rate of state. The state order is the same as the first one.
Description: This analysis is trying to check whether their is a direct relation between the candiate supporting rate and the state 			poverty rate.
Commend Line: python Analysis01.py Hillary 



Analysis02: 
Input: 	State name for short
Output: Two pie plot. The first one shows the distribution of the education degree demography rate of the input state.
		The second one shows the racial demography distribution of the input state.
Description: This Analysis is trying to show you this two demography information of the certain state.
Commend Line: python Analysis02.py CA 

Analysis03: 
Input: 	State name for short
Output: One bar plot and one line plot. The bar plot shows the unemployment rate of the input state from 2007 to 2016.
		The line plot shows the supporting rate of two partys during the last three elections of the input state.
Description: This Analysis is trying to check whether their is a direct relation between the unemployment rate and the supporting rate 			of this two party.
Commend Line: python Analysis03.py CA 
note: This analysis merges two data source and make a new dataframe object

Analysis04: 
Input: 	One year number from 2005 to 2014
Output: One bar plot. The output bar plot shows the median household income for all state in US in the certain year. And shows the US average household income as a threshold line.
Description: This Analysis is trying to show you the income condition for all the state in US, and tell you which one is lower than the US line and which one is higher.
Commend Line: python Analysis04.py 2013
note: This analysis concat a few data source and make a new dataframe object

Analysis05: 
Input: 	State name for short
Output: One state map. The map show you the unemployment rate of every county in this state.
Description: This Analysis is trying to show you the unemployment condition in certain state.
Commend Line: python Analysis05.py CA
note: This analysis use data visualization api bokeh