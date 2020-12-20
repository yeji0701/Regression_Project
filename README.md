Regression_Project

Predicting the Movie's Revenue and Audience with Linear Regression Model.
=========================================================================
When having a data which we could know before a film was released, what would the Revenue and Audience of the film be predicted?
We strove to find out the best Linear Regression Model to predict its Revenue and Audience.

Prerequisites:
* Jupyter Notebook
* Python3
* Anaconda

Getting Started
---------------
##### Packages to install
* matplotlib.pyplot
* seaborn
* warnings
* pandas
* numpy
* sklearn.preprocessing
* sklearn.model_selection
* sklearn.linear_model
* sklearn.metrics


##### Dataset
- (811rowsx10columns)
- Feature
  * Number of Screen
  * Genre
  * Distributor
  * AgeRate
  * Release Date (month,year,season)
  * Actor
- Label
  * Sales 
  * Audience 

Procedure:
-----------------
I. Data Cleansing
- Korean movies from 2008~2020 were used.
- Eliminated movies rated 'Adult'.
- 'Audience', 'Sales' were converted to a million.
- Actors with the same name or one-syllable name were removed from the list.
- A Distributor value was missing and filled in with mode value of Distributor.

II. Data Visualization
![image](https://user-images.githubusercontent.com/72846750/102708827-b0bdb280-42e8-11eb-8d02-0b860dfac2da.PNG)
- Two Histograms of Sales and Audience are right skewed, which means most of movies are struggling to be successful.
  Plus, we found ourselves in trouble to predict those two as imbalance data. 
- Since Number of Screen has correlated closely to the Sales and Audience, the histogram of Screen is right skewed as well.
- We could see that Top 5 Distributor are taking over this industry. 

III. Testing model
1. Label : Audience
![image](https://user-images.githubusercontent.com/72846750/102709442-0a74ab80-42ee-11eb-86a3-a2ba7eabfc0f.png)
- Since Audience Data is placed with the outliers in upper fences, I supposed, if necessary, outliers will be elimated one by one within upper fences.
![image](https://user-images.githubusercontent.com/72846750/102709471-6808f800-42ee-11eb-898e-c48944040a31.PNG)
- Chose to go with a RMSE indication to see how much better the model is than just predicting without adequate data cleansing.
![image](https://user-images.githubusercontent.com/72846750/102709656-be2a6b00-42ef-11eb-8fb7-535317f4dfd8.PNG)
- RMSE of Test Data decreased from 1.73 to 0.75 after continuous data cleansing.


.   
Built with
----------
* 김예지
  * Data gathering through API. Data cleansing process. Data visualizing on the overall movie data. (process 1, 2, and 3 of Data Visualization)
  * Github : https://github.com/yeji0701
* 방희란
  * Data cleansing, Data visualizing and Testing model on Audience.
  * Github : https://github.com/Heeran-cloud
 
Acknowledgements
----------------
- [KOBIS](http://www.kobis.or.kr/kobis/business/main/main.do)
