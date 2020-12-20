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
  * Sales Amount
  * Audience Amount

Procedure:
-----------------
I. Data Cleansing
- Korean movies from 2008~2020 were used.
- Eliminated movies rated 'Adult'.
- 'Audience', 'Sales' were converted to a million.
- Actors with the same name or one-syllable name were removed from the list.
- A Distributor value was missing and filled in with mode value of Distributor.

II. Data Visualization
1. ![image](https://user-images.githubusercontent.com/72846750/102708827-b0bdb280-42e8-11eb-8d02-0b860dfac2da.PNG)
- Two Histograms of Sales and Audience are right skewed, which means most of movies are struggling to be successful.
  Plus, we will be in trouble to predict those two as imbalance data. 
- Since Number of Screen has correlated closely to the Sales and Audience, the histogram of Screen is right skewed as well.
- We could see that Top 5 Distributor are taking over this industry. 

2. ![image]

Built with
----------
* 김예지
  * Data gathering through API. Data cleansing process. Data visualizing on the overall movie data. (process 1, 2, and 3 of Data Visualization)
  * Github : https://github.com/yeji0701
* 방희란
  * Data cleansing process. Data visualizing on the overall movie data. (process 4, 5 and 6 of Data Visualization)
  * Github : https://github.com/Heeran-cloud
 
Acknowledgements
----------------
- [KOBIS](http://www.kobis.or.kr/kobis/business/main/main.do)
- [Naver movie](https://movie.naver.com/)
