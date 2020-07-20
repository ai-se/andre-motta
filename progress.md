# ICSE Paper Progress

## Finding Baseline

Currently working on reproducing the following paper:

* An Architecture based on interactive optimization and machine learning applied to the next release **problem**

This paper uses genetic algorithms to create solutions for the NRP (next release problem) which is a very similar problem to the product lines one.

They use humans in the loop to score generated candidates and build a database of human evaluation to train a machine learning algorithm to eventually substitute the human. This machine learning would be suited for the opinions on that specific user.

The thing is that this paper only works for a singular expert. Not to amass the knowledge of multiple experts onto a product line / next release

## Lit Review

Underway, there are not many relevant papers in the area and I haven't found one that does multiple human in the loop


## Code:

Currently the code base can:

* Generate N unique solutions for the problem based it is on .dimacs format
* Generate the tree of options based on N unique solutions, we can determine the size of the leaves.
* We can walk through the tree of options
* We can determine which is the best node to be examined considering east/west pair under some criteria. Currently most subtress & less difference.

Currently on the way (Under development):

* Oracle: Need better definition on how to generate this scoring oracle and if possible include the randomized parameters for each node:
    * Total Cost (Cost of the option)
    * Known Defects (Previous Knowledge about option settings defects)
    * Features Used (Features used in previous scenarios)
    * Include the weight measured by humans
    * Include some form of nlp over description text of the feature
* User Interface:
    * Define how to make the question to the user
    * Define how to reflect the input of the user on the tree
    * Prototype in Console App
    * Application on some platform (Web / Desktop app)

## Case Material

Scrum Product Line 

* Map features to description
* Verify for Key features

Look for other databases in splot of products that make sense. SE area products

* Map features to description
* Verify for Key features

## Run the experiments

We still need to finish the interface and oracle before running the experience. Also the criteria for determining the best node to be examined.

At the end it is a search problem in a huge space.

## Questions from want.txt

-   Can you now walk a tree of options for an agile project? 
    -   Yes

-   Can you build an oracle where at every level the options at each half can be score by some oracle 
    (e.g. sentiment analysis based background text from the scrum manual, from the project requirements). 
    - We need a better definition on what to include in the oracle
    
-   Do you have an interface where we can put humans  in front of it? 
        I can get you your humans if you have that interface.  
    - Not yet.