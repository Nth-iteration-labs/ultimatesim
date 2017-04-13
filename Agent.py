# -*- coding: utf-8 -*-
# Import all policies
from policies import *
import numpy as np

class Agent:
    """ Generic agent class
    """
    agentID = 1
    
    def __init__(self, offer, response):
        self.id = Agent.agentID
        Agent.agentID += 1
        
        self.offerRounds = 0
        self.responseRounds = 0
        
        self.offer = offer          # Offer strategy
        self.response = response    # Response strategy
        
        self.data = np.empty([0,7], dtype=int)
        self.profit = 0
     
        
    def printAgentDetails(self):
        print("AgentID", self.id)
        print("Offerpolicy: ", self.offer, ", Response: ", self.response)
        print("====================")
        return(False)
     
        
    def makeOffer(self, partner):
        self.offerRounds += 1
        offer = globals()[self.offer]().doOffer(self.data, partner)
        return(offer)
        
    
    def getResponse(self, offer, partner):
        self.responseRounds += 1
        response = globals()[self.response]().doResponse(offer, self.data, partner)
        return(response)
    
    
    def storeData(self, nround, offerer, offer, response, partner):
        if(response==1):
            self.profit += offer
            
        newrow = np.array([nround, self.id, offerer, offer, response, partner, self.profit], dtype=int)
        self.data = np.vstack([self.data, newrow])
        
        print("The data for agent ", self.id, "is:")
        print(self.data)
    
    
    def getID(self):
        return(self.id)
    
    
    def getCurrentProfit(self):
        return(self.profit)

