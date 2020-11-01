# Progress

## Algorithm Results

After running the recursive split algorithm on the tree asking the relevant questions we select the optimal answer between the ones pre-approved by the user. This is done by selecting the minimum scoring answer to the following minimization equation.

* (totalCost)<sup>2</sup> + (knownDefects)<sup>2</sup> + (124 - featuresPreviouslyUsed)<sup>2</sup> + 1.5*(100 - selectedPoints)<sup>2</sup>

This in turn is compared to all the solutions available in the search space. And we extract the percentile of our solution compared to the entire search space.

This processed was repeated 20 times and I ran a scott-knott test on the results.

`Score (*------------------------|------------------------), 0.010,  0.010,  0.010,  0.015,  0.015`

This in turn means that our solution is on the bottom 1% percentile in this minimization task.


## Baseline


After running the Baseline algorithm on the same problem we noticed a few things.

The minimization equation in this case is very similar being

* (totalCost)<sup>2</sup> + (knownDefects)<sup>2</sup> + (124 - featuresPreviouslyUsed)<sup>2</sup> + 1.5*(100 - userScore)<sup>2</sup>

Where userScore is an arbitrary score the user gives to the problem between 0 and 100.


This in turn is compared to all the solutions available in the search space. And we extract the percentile of the selected solution compared to the entire search space.

Noticed problems with this approach.

* We ask humans to look at full instances of the problem which show 124 features and 3 numbers (totalCost, knownDefects, featuresPreviouslyUsed). To ask a person to score such a rich instance is very likely a problem due to cognitive biases and problems related to the comparison of too many variables at once (We have authoritative statements from other papers to back this)

* If we don't ask enough questions to humans out of the initial population of 10000 solutions, we can't really train the MLPRegressor enough to be able to predict the scores going forward which means the GA doesn't evolve. Which brings out another problem of cognitive bias.

* The mutated solutions might not be valid at all given the constraints of the problem. In fact it's much more likely that the mutated solution is not valid.

* How to develop an oracle to score a product in this situation. We will follow the steps of the oracle baseline.

So, although there is much to fix on the baseline reproduction there are various points to be made already on the framework of the baseline solution. And how we can improve on that.

## Next Step

1 - Find authoritative statements comparing the two problems (NRP and Product Lines).
* Hopefully find something that argues their similarity.

2 - After the reproduction code is complete. Compare the solutions.
* Since the paper produces only 1 solution at the end we could compare the minimization properties of that solution against the initial generated population. Or we can run Cohen's d test to validate it.



