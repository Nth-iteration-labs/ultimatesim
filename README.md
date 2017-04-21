# Ultimatesim
Agent based simulations of iterated ultimatum game.

The ultimatum game is a simple two player game. In the game the offerer makes 
an offer to the responder (in the current implementation the offer will be in 
0-10 in integer values) and subsequently the responder either accepts the offer
or rejects the offer [0,1]. If the offer is accepted both receive what was offered,
if not, both players receive no payoff.

The tendency of humans players to a) offer fair shares, and b) decline unfair
offers has been taken as a demonstration of "irrational behavior". Recent 
work shows however that --- in evolutionary simulations --- fairness evolves
in single iterations of the game (see: http://www.pnas.org/content/110/7/2581.full).

The current software aims at making it easy to experiment with different offering
and response strategies in iterated games (hence, players in a population can)
meet the same players again. The current software allows one to specify different
policies for offering and responding; possibly policies that change as a function
of their historical succes. After creating a population in which certain 
response and offer policies are present with pre-specified rates one can run multiple
simulations of iterated games and inspect their behavior.

## The software
The software was primarily written to support our own investigations, but
due to its structure can easily be expanded and used. Below we detail the basic
usgage of the software, provide some minimal examples, and describe how one can
build on the current software.

## Running a simulaiton
After downloading all the files in this repository, running a simulation is easy and,
if one has python 3, numpy, and matplotlib installed, can be done by typing:
```
python main.py
```
in your terminal after navigating to the ultimatesim folder. 

Now, this is not too interesting, but it give you a gist of a small simulation
and produces a few plots. 

For those just wish to use the framework without modifications the above command
together with changes made to the config.py file should satisfy. The examples
below detail the usage of the config.py file.

## Some examples
To specify the parameters of a simulation please make changes to the config.py
file. Most of the content of that file should be self explanatory, but for completeness
we provide an exmple here. We setup a simulation by first setting up the 
population of agents:
```python
#### First, we define the population
# Population size (e.g., the number of agents in the population:
popSize = 100

# An array describing the offering policies in the population:
# see the /policy folder for the options
offerPolicies = np.array(["REMOffer", "RandomOffer"], dtype=str)

# An array describing the response policies in the population:
responsePolicies = np.array(["REMResponse", "RandomResponse"], dtype=str) 

# A matrix (who's entries should sum to 1) describing the probabiltiy
# of occurancy of different strategy combination in the population
# Columns denot offer policies, rows denote response policies
probMatrix = np.matrix([[.7,0.1],[0.1,0.1]])
```


## Creating and agent

### Furthere expanding the software

## To do's / future development


## More info & questions
