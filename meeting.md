# Meeting 09/04

## LexisNexis

Generating Report with Xiao over the weekend for next's weeks meeting

## CSC 510 

Currently Reading through Results.md files

## Linux Foundation

Coccicheck is working and we are able to find the same bugs from the file provided running coccicheck on the kernel. 
We are also able to run coccicheck on the Zephyr code.

There are some bugs in the coccicheck code for linux. But the fix is simple. Need to pass it to Sherry!

## PhD

Code is now rewritten. Wasn't able to run the experiment yet. Should have results by monday.

Now the code is doing hard selections and pruning the tree to select a singular leaf by the end of the search. The number of comparisons in a singular question will now vary and we select the minimum number of questions whenever possible in order to be able to prune the tree.
This would also theoretically make it so that currently in this deterministic system the minimum number of questions we ask is `root(n)` where `n` is the number of configurations. 
The maximum theoretical number of questions becomes `n` for a problem with `n` features and `n` configurations. This would be very unlikely however. Since we are able to generate configurations to a defined number so that:
* `configurations > features` 
* `root(configurations) < features`.

At the end we will have selected a leaf node with `root(n)` items. We run an optimizer (PSO or even PyGMO) on those items to select the best configuration given the defined goals. 

Multi-goal: 
* Cost/Effort (minimize) 
* User Selected Features (maximize) 
* Previously Used Features (maximize) 
* Known Defects In Configuration (Minimize).

