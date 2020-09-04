# Meeting 09/04

## LexisNexis

Generating Report with Xiao over the weekend for next's weeks meeting

## CSC 510 

Currently Reading through Results.md files

## Linux Foundation

Coccicheck is working and we are able to find the same bugs from the file provided running coccicheck on the kernel. 
We are also able to run coccicheck on the Zephyr code.

## PhD

Code is now rewritten. Wasn't able to run the experiment yet. Should have results by monday.

Now the code is doing hard selections and pruning the tree to select a singular leaf by the end of the search. The number of comparisons in a singular question will now vary and we select the minimum number of questions whenever possible in order to be able to prune the tree.

At the end we have selected a leaf node with 100 items. We run an optimizer (PSO) on those items to select the best configuration. 

Multi-goal: 
* Cost/Effort (minimize) 
* Selected Features (maximize) 
* Previously Used Features (maximize) 
* Known Defects In Configuration (Minimize).

