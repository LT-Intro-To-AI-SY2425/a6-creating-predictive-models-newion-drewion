# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

Less accurate. This is because the estimated salaries are much greater numbers than the other two, meaning it poorly influences the model's trianing

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

Much more accurate, around 85%. This is not enough for a major dealership to actually make decisions based on this model's predictions of whether someone will buy a car, since there's so much money at stake with such an expensive item. This could work for other use cases, though, like for stores that sell more common household goods. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

Overall, the model did well. That said, people with "average" salaries were hard to classify, as well as rich young people and not so rich old people, since there less data on those two groups. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

No, the person would not buy the suv.