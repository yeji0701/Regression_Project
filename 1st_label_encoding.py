import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager
f_path = "C:\Windows\Fonts\malgun.ttf"
font_manager.FontProperties(fname=f_path).get_name()
from matplotlib import rc
rc('font', family='Malgun Gothic')
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# read movie data
movie = pd.read_csv('C:/Users/luvu1/Documents/dss15/Regression_Project/Sales_analysis/datas/final_movie_Rev5.csv', index_col=[0])
movie.reset_index(drop=True, inplace=True)

# label encoding 'Rate' and 'Genre' columns
labelencoder = LabelEncoder()
movie['Rate'] = labelencoder.fit_transform(movie['Rate'])
movie['genre_encoded'] = labelencoder.fit_transform(movie['Genre'])

# separating x and y variables
numerics = ['int64', 'float64', 'int32']
movie_df = movie.select_dtypes(include=numerics)
X = movie_df.drop(['Sales', 'Audience'], axis=1)
y = movie_df['Sales']

# split x and y variables to train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

# fit Linear Regression and predict to test data
reg = LinearRegression()
reg.fit(X_train, y_train)
pred_tr = reg.predict(X_train)
pred_test = reg.predict(X_test)
rmse_tr = (np.sqrt(mean_squared_error(y_train, pred_tr)))
rmse_test = (np.sqrt(mean_squared_error(y_test, pred_test)))
print('RMSE of Train Data : ', rmse_tr)
print('RMSE of Test Data : ', rmse_test)

## plot can be viewed through jupyter notebook
# scatter plot of prediction on 'Actual Sales' and 'Predicted Sales'
sns.set_style('darkgrid')
plt.scatter(y_test, pred_test)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.plot([0,50000], [0,50000], 'r');