# Literature Statements

## Statement 1

Given the emerging state of the iSBSE field, there appears to be a general lack of readily agreed and available benchmark case studies and standards. Considering the presence of human interaction with search, statistical analysis is appropriate, although it is recognized that this might be difficult if the sample size (in terms of number of participants and problem instances) is small. To address this, we note that Arcuri and Briand offer a helpful guide to statistical tests for assessing randomized algorithms in software engineering [47], and Neumann et al. suggest a useful executable experimental template pattern for the systematic comparison of metaheuristics [72].

**Proposed solution**

  1. Run the solution on Mechanical Turk.  (Build a benchmark/standard with big data from humans)
  2. Do appropriate testing of the randomized algorithm (Oracle - Arcuri and Briand). 
  3. Follow a standard template for the comparison of different metaheuristics. (Weighting scheme and decision process within selected cluster of solutions – Neumann et al.)

## Statement 2

The lack of iSBSE studies in the areas of source code implementation and project management would seem to indicate a gap in the field.

**Proposed solution**

  1. There are no studies on iSBSE on project management automation. Or the selection of project management rule template. So simply by writing this with good results we are filling a gap in the literature

## Statement 3

In addition, we speculate that incorporating expert knowledge into search in iSBSE represents a gap in the field. As is typical in metaheuristic search, sources in the review initialize populations of solution individuals either at random or according to domainspecific heuristics. However, the reuse of expert knowledge (e.g., patterns, benchmarks etc.) to initialize populations might offer possibilities.

**Proposed solution**

  1. Use the acquired knowledge (during search) to insert soft crosstree constraints to redefine the search space.
  2. Use previously known knowledge from the area to pre-insert some soft crosstree constraints.

# Code advances.

## Hard vs Soft decisions

It seems that working on Soft decisions creates room for many problems down the line. The main advantage of using a dendrogram (Tree Cluster) 
would be the fact that you can eliminate many options by simply asking questions about one node. By using soft goals we lose that advantage since a question does not necessarily wipe out
anything from the tree. The search becomes then almost linear `O(n)` to the number of tree nodes (discounting leaves) instead of operating in `O(log(n))`.

The code is being rewritten to now use hard decisions. This would allow for exploiting the most important feature of the dendogram. By making a decision we can effectively stop searching at any nodes contrary to the decision made beforehand.
The experiment with the Random oracle will be rerun by next week under these circunstances.


## Multi-Goal Problem

We have now inserted into the codebase multiple goals related to the different features, them being:
 
  * Effort : The cost (money/time/resources needed for each feature)
    * which we want to minimize for the whole solution
  * Previous uses: How many of these features have been successfuly used before 
    * which we want to maximize for the whole solution
  * Known problems: How many of these features have known problems
    * which we want to minimize for the whole solution
    
The idea then is to by using hard decisions find the cluster that better represent the user decisions, and in that cluster of `log(n)` leaves run an multi-goal optimizer in order to select the best solution for the following goals:

  * Adequacy to the user input (We want to maximize selected options in previous questions)
  * Minimum cost
  * Most previous uses
  * Less known defects
  
## Added requirements to diminish cognitive bias in the model and also build user trust in the iSBSE algorithm.

* The user should be able to go back on decisions, similarly to a ctrl-z which would regress to the previous state of the tree descent. 
* The user should also be able to see all the features that have been currently wiped out by previous decisions.
* The user should be able to select an item from the wiped out features and insert them as a requirement to their solution. If there is a constraint related to another previously selected item, the user should be asked to pick whichever he thinks it's more important.

# Multi-human 

Open question:
* Should we work on having multiple users select from the same tree and use multiple-user input to select the best project or should we do an ensemble of dendrograms to select the best cluster for most users?
* Should we try to find the best for all users or should we cluster similar users and select teams that work the best together on agile projects based on similar culture and expectations in the scrum process?




