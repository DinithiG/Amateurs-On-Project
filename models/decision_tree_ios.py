import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import re
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import warnings


data = pd.read_csv("/Users/firefly0118/Documents/uni/L5 - second year/semester 1/SDGP/Intellihack/AppleStore.csv") 
data.head() #first five rows of the table
print(data.columns)
columns_to_drop = ['id', 'currency', 'rating_count_tot','rating_count_ver','user_rating_ver','ver','cont_rating', 'sup_devices.num','ipadSc_urls.num','vpp_lic']
data.drop(columns=columns_to_drop, inplace=True)
data.head()
# Rename columns in place >>>>>This code will already be exectued
data.rename(columns={'price':'price_dollars'}, inplace=True)
data.head()
available_categories = data['prime_genre'].unique()
print(available_categories)
# encode categorical variables
encoder = LabelEncoder()
data['prime_genre'] = encoder.fit_transform(data['prime_genre'])
print(data['prime_genre'].unique())
# select the relevant features and target variable
X = data[['size_bytes','price_dollars','prime_genre','lang.num']]
y = data['user_rating']

# select the relevant features and target variable
X = data[['size_bytes', 'price_dollars', 'prime_genre', 'lang.num']]
y = data['user_rating']

# replace infinite and NaN values with 0
X = X.replace([np.inf, -np.inf, np.nan], 0)
y = y.replace([np.inf, -np.inf, np.nan], 0)

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the model on the training set
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)


# predict the target variable for the test set
y_pred = model.predict(X_test)

# calculate r2-score, mean absolute error, and root mean squared error
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# calculate accuracy as percentage of the mean absolute error
accuracy = 100 * (1 - (mae / y_test.mean()))

print(f"The r2-score of the model is {r2:.2f}")
print(f"The mean absolute error of the model is {mae:.2f}")
print(f"The root mean squared error of the model is {rmse:.2f}")
print(f"The accuracy of the model is {accuracy:.2f}%")