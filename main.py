# -*- coding: utf-8 -*-
"""
Created first on Tue Apr  4 09:08:17 2017

@author: Dr. M.C. Kaptein

A litlle software library for running simulations of the ultimatum game

"""

# Imports
from Simulation import Simulation
import numpy as np
#np.set_printoptions(threshold=np.nan)
import config


# Retrieve settings:
numberOfSims = config.nSims
simLength = config.simLength
populationSize = config.popSize
offerPolicies = config.offerPolicies
responsePolicies = config.responsePolicies
policyOccuranceMatrix = config.probMatrix

# Print settings 
print("Running a new simulation with the parameters:")
print("Population size: "+str(populationSize))
print("Number of simulations: "+str(numberOfSims))
print("Number of rounds per simulation:"+str(simLength))
print("And the following distribution over policies:")
print(policyOccuranceMatrix)
print("Columns:")
print(offerPolicies)
print("Rows:")
print(responsePolicies)




# Runt the simulations:
simulation = Simulation(numberOfSims, name="Test")
simulation.Initialize(simLength, populationSize, offerPolicies, responsePolicies, policyOccuranceMatrix, storeall=False)
simulation.Run(verbose=True, save=True)

# Get results of simulations
print("The average bid per round is:")
simulation.plotAverageBid()
print("The average profit per round is:")
simulation.plotAverageProfit()
print("The average response per round is:")
simulation.plotAverageResponse()

