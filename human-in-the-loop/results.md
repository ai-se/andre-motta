# Score Scott Knott Test

    Score (*                        |                        ), 0.010,  0.010,  0.010,  0.015,  0.015
    
We calculate the item score with the sum of squares function. We want to minimize the whole score so we reverse the value for
Previously Used Features and Percentage of User Selected Features Awarded

The formula to minimize is as follows 

    x.totalcost^2 + x.knowndefects^2 + (124-x.featuresused)^2 + 1.5*(100 - x.selectedpoints))^2
    
The 1.5* is a 50% weight increase to the user opinion and is a parameter that can be tweaked and optimized to different problems.

Then we calculate the percentile of the score relative to all the items in the tree. Even non selected items. We can see that no matter how the user chooses we end up
at the bottom 1% of the percentiles, and since this is a minimization problem this is a great result.

## Next Steps

* Implement the baseline algorithm
* Use **Cohen's D** test to calculate the performance of my algorithm against it, since the baseline only outputs one item.
* Compare both the process and results.