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
