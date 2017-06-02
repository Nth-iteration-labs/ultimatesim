# -*- coding: utf-8 -*-
import numpy as np

#### Congifuration file for UltimateSim, a little package
# to simulate iterated ultimatum games in mixed player 
# populations



#### First, we define the population
# Population size (e.g., the number of agents in the population:
popSize = 200

# An array describing the offering policies in the population:
# see the /policy folder for the options
offerPolicies = np.array(["THOMP1Offer", "RANDOMOffer"], dtype=str)

# An array describing the response policies in the population:
responsePolicies = np.array(["THOMP1Response", "RANDOMResponse"], dtype=str) 

# A matrix (who's entries should sum to 1) describing the probabiltiy
# of occurancy of different strategy combination in the population
# Columns denot offer policies, rows denote response policies
probMatrix = np.matrix([[.7,.1],[.1,.1]])



### Next, we specify the simulations
# Simulation length; the number of rounds played
# per simulation
simLength = 50

# Number of sims; the total number of simulations to run with this setting:
nSims = 50



### And finally, we determine the output of this simulations:
# Create outut plots (put this to true, otherwise nothing really happens ;))
createPlots = True    
    
# Store all rund to /data folder as csv?
# This could generate a lot of data if you run many long simulations
storeAll = False