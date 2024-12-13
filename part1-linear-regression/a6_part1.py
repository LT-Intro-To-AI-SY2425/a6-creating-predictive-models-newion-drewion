import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)
model = LinearRegression().fit(x,y)
plt.figure(figsize=(10,6))

coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x,y)
print(intercept)
# Create the model

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 


# Print out the linear equation and r squared value
print(str(2))
# Predict the the blood pressure of someone who is 43 years old.
prediction = model.predict([[42]])
# Print out the prediction
print(str(prediction))
plt.plot(x, coef*x + intercept, c = "purple", label = "best fti")
plt.scatter(x,y)
# Create the model in matplotlib and include the line of best fit
plt.legend()
plt.show()