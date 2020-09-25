# Progress

## Algorithm Results

After running the recursive split algorithm on the tree asking the relevant questions we select the optimal answer between the ones pre-approved by the user. This is done by selecting the minimum scoring answer to the following minimization equation.

* (totalCost)<sup>2</sup> + (knownDefects)<sup>2</sup> + (124 - featuresPreviouslyUsed)<sup>2</sup> + 1.5*(100 - selectedPoints)<sup>2</sup>

This in turn is compared to all the solutions available in the search space. And we extract the percentile of our solution compared to the entire search space.

This processed was repeated 20 times and I ran a scott-knott test on the results.

`Score (*------------------------|------------------------), 0.010,  0.010,  0.010,  0.015,  0.015`

This in turn means that our solution is on the bottom 1% percentile in this minimization task.


## Next Step

1 - Sort out the errors in PyGMO on reproducing:
* An Architecture based on interactive optimization and machine learning applied to the next release **problem**

2 - Find authoritative statements comparing the two problems (NRP and Product Lines).
* Hopefully find something that argues their similarity.

3 - After the reproduction code is complete. Compare the solutions.
* Since the paper produces only 1 solution at the end we could compare the minimization properties of that solution against the initial generated population. Or we can run Cohen's d test to validate it.
