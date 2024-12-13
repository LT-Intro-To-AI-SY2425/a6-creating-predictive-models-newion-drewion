# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

The R squared value represents the difference in car prices that the model predicts. in relation to the data, if the r^2 value is 0.86 (in this case), that means the model has an accuracy of around 86%

2. Is your model accurate? Why or why not?

The r^2 value is pretty solid at aronud 0.86 or 86%, but isn't perfect and could use some more testing data. 

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

89000 and 10:::: 14058.14
1500000 and 20:::: 10348.43

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Because of how the formula is for predicting results, the inputs for miles and age can eventually outweigh the value of the intercept. This is probably happening because the extreme ends of car values aren't included as training data, meaning it doesn't know how to handle a car that's worth very little.  