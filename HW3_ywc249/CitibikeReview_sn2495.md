## 1. Hypotheses 
The Null hypotheses has been formulated correctly. Great Job! Would be even better if the significance level was mentioned.


Yuwen wanted to check if the average trip length on weekends is greater than that of weekdays.

For the question raised, the Null hypothesis was set as:
* The avaerage trip duration on weekends is the same as or less than that of weekdays*

The alternative hypothesis has been formulated and shown as H1: T(weekend)> T(weekday). It would be great if the alternative hypothesis has also been expressed as a sentence like the null hypothesis.



## 2. Data
The data has the appropriate features (variables) to answer the question but not directly. The weekday/weekend information had to be extracted from the date information. The required info was extracted from the given information in an elegant way. Good Job!

Two needed variables is the trip duration and date.
Yuwen has extracted these two columns correctly and dropped all the irrelevant variables.
Then, he extracted the weekday/weekend info from the date column. Used group by to get the average trip durations for each day of the week. This allowed him to plot the average for each day and also for the weekday vs weekend.

## 3. Test
To test H0 given the type of data and the question asked, I prefer to choose the t test or the Z test.
Yuwen applied the t-test to the data and concluded that the null hypothesis cannot be rejected. Great job picking the test and applying it!

Below is the reasoning for choosing t-test or the z-test
I follow the chart presented in the lecture slides. The following is the path 
1. Do samples come from same or different populations
2. Assume the data is parametric
3. Number of categories is 2
4. Data is not paired
5. if we assume variance is same, then we use Z-test else we use Welch t test.


