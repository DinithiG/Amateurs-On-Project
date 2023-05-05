import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
import re
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import warnings

data = pd.read_csv("/Users/firefly0118/Documents/uni/L5 - second year/semester 1/SDGP/Intellihack/AppleStore.csv") 
data.head() #first five rows of the table

# Rename columns 
data.rename(columns={'price':'price_dollars'}, inplace=True)

# encode categorical variables
encoder = LabelEncoder()
data['prime_genre'] = encoder.fit_transform(data['prime_genre'])

# select the relevant features and target variable
X = data[['size_bytes', 'price_dollars', 'prime_genre', 'lang.num']]
y = data['user_rating']

# replace infinite and NaN values with 0
X = X.replace([np.inf, -np.inf, np.nan], 0)
y = y.replace([np.inf, -np.inf, np.nan], 0)

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# perform hyperparameter tuning
param_grid = {
    'C': [0.1, 1, 10],
    'epsilon': [0.01, 0.1, 1],
    'kernel': ['linear', 'rbf', 'poly']
}
model = SVR()
grid_search = GridSearchCV(model, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)

# select the most important features
from sklearn.feature_selection import SelectKBest, f_regression
selector = SelectKBest(f_regression, k=3)
selector.fit(X_train, y_train)
X_train_new = selector.transform(X_train)
X_test_new = selector.transform(X_test)
print(selector.get_support())

# train the model on the training set with the best hyperparameters and selected features
model = SVR(**grid_search.best_params_)
model.fit(X_train_new, y_train)

# predict the target variable for the test set
y_pred = model.predict(X_test_new)

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