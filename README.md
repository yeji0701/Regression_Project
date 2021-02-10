Regression_Project

Predicting Movie Revenue and Number of Audience with Linear Regression
======================================================================
After the EDA with the Korean movie data, we decided to continue on with predicting sales and number of audience of a film. In this Regression Project, Linear Regression model was used from the beginning with various manipulation of the column data and calculated RMSE(Root Mean Squared Error) to evaluate the difference between actual and predicted value. 

Getting Started
---------------
##### Packages to install
- this project was built on Python 3 with following installations:
```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install scikit-learn
```
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
- [detailed visualization outcome](https://github.com/dss-15th/reg-repo-5/blob/master/Sales_analysis/01_Sales_visualizing.ipynb)
- [detailed data exploration](https://github.com/dss-15th/reg-repo-5/blob/master/Sales_analysis/04_Sales_data_exploring.ipynb)

III. Testing model
- chose to  with a RMSE indication to see how much better the model is than just predicting without adequate data cleansing.
- proceeded testing in 4 different ways:
  * [Applying ordinal encoder on 'Rate' and 'Genre' (additionally 'Distributor' column for Audience label) columns](https://github.com/dss-15th/reg-repo-5/blob/master/1st_label_encoding.py)
  * [One-hot encoding 'Rate', 'Genre', 'Season', 'Year', 'Month' columns](https://github.com/dss-15th/reg-repo-5/blob/master/2nd_onehot_encoding.py)
  * [Removing outliers of quantile 25 and 75 in additional to one-hot encoding](https://github.com/dss-15th/reg-repo-5/blob/master/3rd_onehot_encoding%2Bremove_outliers.py)
  * [Second removal of outliers to 3rd trial](https://github.com/dss-15th/reg-repo-5/blob/master/4th_onehot_encoding%2Bremove_outliers_twice.py)
1. Label : Audience
  ![image](https://user-images.githubusercontent.com/72846750/102709442-0a74ab80-42ee-11eb-86a3-a2ba7eabfc0f.png)
  * Since Audience Data is placed with the outliers in upper fences, I supposed, if necessary, outliers will be elimated one by one within upper fences.
  ![image](https://user-images.githubusercontent.com/28764376/106708564-6c873700-6636-11eb-9188-ffda84190e7b.png)
  * RMSE of Test Data decreased from 1.73 to 0.75 after continuous data cleansing.
2. Label : Sales
  ![image](https://user-images.githubusercontent.com/28764376/106715074-04d5e980-6640-11eb-89de-9804f2d00b92.png)
  * values of Sales is very skewed, which lead to removing outliers.
  ![image](https://user-images.githubusercontent.com/28764376/106708498-52e5ef80-6636-11eb-91d7-b0354c70f212.png)
  * RMSE of Test Data decreased from 12,893.35 to 3,892.27 after continuous data cleansing.

Conclusion
----------
We could say that the process of one-hot encoding and removal of outliers performed well on predicting the number of 'Audience'. As for 'Sales', although the RMSE decreased greatly, we could not say the same process predicted well. First because, the value was too big to intuitively see if the last RMSE is small enough to say it is a good predicted value. Second, there was no data of cost for each movie which we think is an important feature to know the revenue. 
(Detailed procedures and graph outcomes can be viewed from Jupyter Notebook in Sales_analysis folder)
- the prediction results of first two ways differentiated the use of ordinal encoder and one-hot encoding
- removing outliers greatly helped decreasing the rmse 
- there could have been other ways to handle with the values less than 1 and the skewed data:
  * removing data that lies below a certain point we assign (ex. drop rows with sales below 1,000,000)
    ```
    dele = movie[movie['Sales'] < 1].index
    movie.drop(dele, inplace=True)
    ```
    - through this, the rmse decreased from 13,174.05 to 4,128.56 [detailed procedure](https://github.com/dss-15th/reg-repo-5/blob/master/Sales_analysis/08_Sales_feedback_test(drop.sales%20below%201).ipynb)
  * calculating the log value of sales to normalize skewed data
    ```
    movie['log_sales'] = np.log1p(movie['Sales'])
    ```
    - rmse decreased from 1.5 to 1.1 [detailed procedure](https://github.com/dss-15th/reg-repo-5/blob/master/Sales_analysis/08_Sales_feedback_test(log_sales).ipynb)
    
Built with
----------
* 김예지
  * Data cleansing, visualizing, and testing model on Sales.
  * Jupyter notebook code all code files upload, additional trials of removing data and converting to log values after presentation and conclusion
  * Github : https://github.com/yeji0701
* 방희란
  * Data cleansing, Data visualizing and Testing model on Audience.
  * Github : https://github.com/Heeran-cloud
 
Acknowledgements
----------------
- [KOBIS](http://www.kobis.or.kr/kobis/business/main/main.do)
