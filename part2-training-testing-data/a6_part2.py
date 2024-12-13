import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values
print(x,y)
# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)
# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1,1)
print(xtrain, ytrain)
# Create the model
model = LinearRegression().fit(xtrain, ytrain)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
# Print out the linear equation and r squared value:
print("y=", coef, "x=",  intercept)
print(model.score(xtrain, ytrain))
'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
x = x.reshape(-1,1)
# get the predicted y values for the xtest values - returns an array of the results
prediction = model.predict(x)
# round the value in the np array to 2 decimal places
predict = np.around(prediction, 2)
# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for index in range (len(xtest)):
    actual = ytest[index]
    predicted_y = prediction[index]
    xcoord = xtest[index]
print("x: ", float(xcoord), "Y prediction / Y actual: ", predicted_y, actual)

'''
**********CREATE A VISUAL OF THE RESULTS**********
'''

plt.figure(figsize=(10,6))
plt.scatter(xtrain, ytrain, c="purple", label = "Training Data")
plt.scatter(xtest, ytest, c="blue", label = "testing data")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, coef*x + intercept, c="r", label="line lol")

plt.legend()
plt.show()