# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:08:17 2017

@author: Dr. M.C. Kaptein

Library for running simulations of the ultimatum game

"""

# Imports
from Simulation import Simulation
from Population import Population
import numpy as np
np.set_printoptions(threshold=np.nan)



# Settings:
numberOfSims = 50
simLength = 1000
populationSize = 50
offerPolicies = np.array(["THOMP1Offer"], dtype=str)
responsePolicies = np.array(["THOMP1Response"], dtype=str)
policyOccuranceMatrix = np.matrix([[1]])

# Runt the simulations:
simulation = Simulation(numberOfSims)
simulation.Initialize(simLength, populationSize, offerPolicies, responsePolicies, policyOccuranceMatrix, storeall=True)
simulation.Run(verbose=True, save=True)

# Get results of simulations
simulation.plotAverageReward()
simulation.plotAverageProfit()
simulation.plotAverageResponse()

