# -*- coding: utf-8 -*-
from Agent import Agent
import numpy as np


class Population:
    """ Class for generating a population of agents and running a simulation
    """
    
    # Initialize a population
    def __init__(self, agentCount):
        
        if agentCount % 2 != 0:
            raise ValueError("The number of agents needs to be even")
        
        self.agentCount = agentCount
        self.agents = np.empty(agentCount, dtype=object)
        self.rounds = 0
        self.data = np.empty([0,6], dtype=float)
        

    # Populate a poulation with repsonse trategies
    def populate(self, offerPolicies, responsePolicies, probMatrix):
        
        # Check policy matrix
        #if(np.sum(probMatrix) != 1):
        if abs(np.sum(probMatrix) - 1) > 1e-10:
            raise ValueError('The sum of the probablity matrix should be 1')
            
        for i in range(0,self.agentCount):
            options = np.r_[0:probMatrix.size]
            draw = np.random.choice(options, 1, p=np.atleast_1d(np.array(probMatrix.flatten()).squeeze()))
            
            j = 0
            while draw-responsePolicies.size > 0:
                draw = draw-responsePolicies.size
                j += 1

            self.agents[i] = Agent( offerPolicies[j], responsePolicies[int(draw%responsePolicies.size)] )
            
    
    # Play a single round for all agents
    def play(self, rounds):
              
        for n in range(rounds):
            # Select half for offering and shuffle
            select = np.array(np.random.choice(np.r_[0:self.agentCount], 
                                               size=int(self.agentCount/2), replace=False), dtype=int)
            offerers = np.r_[0:self.agentCount][select]
            responders = np.delete(np.r_[0:self.agentCount],select)
            np.random.shuffle(responders)
            
            # Create some arrays for monitoring data
            offers = np.empty(offerers.size)
            profits = np.empty(offerers.size)
            accepts = np.empty(offerers.size)
            
            # print("============ \nRound number: " ,n, "\n =============")
        
            for i in range(offerers.size):
                # Get offer and response
                offer = self.agents[offerers[i]].makeOffer(self.agents[responders[i]].getID())
                response = self.agents[responders[i]].getResponse(offer, self.agents[offerers[i]].getID())
            
                self.agents[offerers[i]].storeData(self.rounds, 1, offer, response, self.agents[responders[i]].getID())
                self.agents[responders[i]].storeData(self.rounds, 0, offer, response, self.agents[offerers[i]].getID())
                offers[i] = offer
                profits[i] = (10*response)
                accepts[i] = response
            
            # Compute some stats and store
            # Variance is not correct!
            self.rounds += 1
            newrow = np.array([float(self.rounds), 
                               np.mean(offers), 
                               np.var(offers),
                               np.mean(profits),
                               np.var(profits),
                               np.mean(accepts)],
                               dtype=float)          
            self.data = np.vstack([self.data, newrow])
    
    
    def getNumberOfAgents(self):
        print("Total number of agents in the population %d" % self.agentCount)
        
    
    def getNumberOfRound(self):
        print(self.rounds)
    
    
    def printAgents(self):
        for agent in self.agents:
            agent.printAgentDetails()
    
    def getData(self):
        return(self.data)
