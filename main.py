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



# Settings:
numberOfSims = 1
simLength = 2
populationSize = 10
offerPolicies = np.array(["REMOffer"], dtype=str)
responsePolicies = np.array(["REMResponse"], dtype=str)
policyOccuranceMatrix = np.matrix([[1]])

# Runt the simulations:
simulation = Simulation(numberOfSims)
simulation.Initialize(simLength, populationSize, offerPolicies, responsePolicies, policyOccuranceMatrix, storeall=True)
simulation.Run(verbose=True, save=True)
simulation.printData()

# Get results of simulations
simulation.plotAverageReward()
simulation.plotAverageProfit()

