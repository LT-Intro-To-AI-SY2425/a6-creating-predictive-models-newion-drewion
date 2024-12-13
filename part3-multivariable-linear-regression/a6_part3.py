import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values
print(data)
#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2)
#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)
#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
co = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y), 2)
print("RSQUARED HERE::::::")
print(r_squared)
#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")

prediction = np.around((model.predict(xtest)), 2)
for index in range (len(xtest)):
    actual = ytest[index]
    predicted_y= prediction[index]
    x_coord = xtest[index]
    print("miles: ", x_coord[0], "Age: ", x_coord[1], "Actual: ", actual, "Predicted", prediction)

print("CAR VALUE PREDICTIONS")
cars = [[89, 10], [150, 20]]
predictions = np.around(model.predict(cars), 2)
print(predictions)