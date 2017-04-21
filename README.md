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
offerPolicies = np.array(["REMOffer", "RANDOMOffer"], dtype=str)

# An array describing the response policies in the population:
responsePolicies = np.array(["REMResponse", "RANDOMResponse"], dtype=str) 

# A matrix (who's entries should sum to 1) describing the probabiltiy
# of occurancy of different strategy combination in the population
# Columns denot offer policies, rows denote response policies
probMatrix = np.matrix([[.7,0.1],[0.1,0.1]])
```
Note that this generates a population with 100 agents of which (in expectation)
70% of the agents have the "Rational Economic Man" (REM) offering policy (e.g., always
offering 1 assuming that it will be accepted), and the REM response policy. About
10% of the agents have a REM offering policy, but a (uniformly) random response
strategy (and so on). This provides a fairly flexible way of setting up
populations with agents following different strategies.

After setting up the popultation we setup the details of the simulation; this 
should be relatively self-explanatory:
```python
### Next, we specify the simulations
# Simulation length; the number of rounds played
# per simulation
simLength = 100

# Number of sims; the total number of simulations to run with this setting:
nSims = 100
```
And finally, we determine the output of this simulations:
```python
# Create outut plots (put this to true, otherwise nothing really happens ;))
createPlots = True    
    
# Store all rund to /data folder as csv?
# This could generate a lot of data if you run many long simulations
storeAll = False
```

Running
```
python main.py
``` 
now produces (amongst others) the following plots:
*![Average offers](/examples/offers.png)
*![Average response](/examples/response.png)
*![Average profits](/examples/profit.png)

And from there on one can start experimenting with different policies, in
different proportions, etc. etc.

## Creating and agent

Now the above use is still not very intersting, the more interesting part of
the library is the ability to create new agents that determine their behavior
based on historical response. This can be done be creating a new offer or
repsonse policy in the /policies/ folder, and inheriting from the base offer
and response policies. For examples, please see the currently implemented policies.

We will add a list describing the available agents shortly.

### Further expanding the software

We are quite well aware that we are missing a bunch of nice to have and
neat to have functionality, but we are trying to push this forward gradually. Things
we would like to add still:
* More overview statistics
* Flexible rules of the game
* More policies
* Evolution / fittness and birth / death of agents
* etc.
On the last point it is interesting to see that evoution (e.g, birht-death of
agents based on fittness) seems very similar to "learning" agents in repeated 
games.

## More info & questions
For more info and contact details see: http://www.nth-iteration.com
