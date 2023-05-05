import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# load the data
data = pd.read_csv("/Users/firefly0118/Documents/uni/L5 - second year/semester 1/SDGP/Intellihack/repo/Amateurs-On-Project/models/googleplaystore .csv")

columns_to_drop = ['Type', 'Content Rating', 'Genres','Last Updated','Current Ver','Android Ver', 'Rating','Reviews']
data.drop(columns=columns_to_drop, inplace=True)
data.head()

# Rename columns in place
data.rename(columns={'Size':'Size Bytes','Price':'Price Dollars'}, inplace=True)
# print unique values in the 'Price Dollars' column
print(data['Price Dollars'].unique())
data.head()

data['Price Dollars'] = data['Price Dollars'].astype(str)
data['Price Dollars'] = data['Price Dollars'].str.replace('$', '',regex=False)
data['Price Dollars'] = data['Price Dollars'].replace('Everyone',np.nan)
print(data['Price Dollars'].dtype)
print(data['Price Dollars'])
data.tail()

data['Price Dollars'] = data['Price Dollars'].astype(float)

# Convert column to string
data['Installs'] = data['Installs'].astype(str)

# Remove "+" and "," characters from "Installs" column
data['Installs'] = data['Installs'].str.replace('+', '').str.replace(',', '')

# Replace "Free" values with NaN
data['Installs'] = data['Installs'].replace('Free', np.nan)

# Convert column to float
data['Installs'] = data['Installs'].astype(float)

# Drop rows with NaN aka not a number values in "Installs" and "Price Dollars" columns
data.dropna(subset=['Installs'], inplace=True)
data.dropna(subset=['Price Dollars'], inplace=True)

# Check data type of column
print(data['Installs'].dtype)
print(data['Installs'])
data.tail()

import re

# Define a function to convert size to bytes
def convert_size(size_str):
    if size_str == 'Varies with device':
        return np.nan

    size, unit = re.match(r"^([\d\.]+)([a-zA-Z]*)$", size_str).groups()
    size = float(size)

    if unit == 'K':
        return size * 1024
    elif unit == 'M':
        return size * 1024 * 1024
    elif unit == 'G':
        return size * 1024 * 1024 * 1024
    else:
        return size

# Apply the conversion function to the 'Size Bytes' column
data['Size Bytes'] = data['Size Bytes'].apply(convert_size)

# Drop rows with missing values in the 'Size Bytes' column
data = data.dropna(subset=['Size Bytes'])

data.head()

available_categories = data['Category'].unique()
print(available_categories)

# encode categorical variables
encoder = LabelEncoder()
data['Category'] = encoder.fit_transform(data['Category'])

# select the relevant features and target variable
X = data[['Category','Size Bytes', 'Price Dollars']]
y = data['Installs']

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
