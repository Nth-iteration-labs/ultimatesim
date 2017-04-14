# -*- coding: utf-8 -*-
import numpy as np

class responsePolicy:
    """ Baseline policy """
    
    def __init__(self):
        self.name = "None"
     
    def doResponse(self, offer, data, partner):
        print("WARNING: DEFAULT RESPONSE")
        return(0)
    
    def printData(self, data):
        print(data)
        
    def getAccepts(self, data):
        sub = data[data[:,1] == self.getMe(data)]     # select my rows
        #print("Me is: ",self.getMe(data))
        #print(sub)
        sub = sub[sub[:,4] == 1]                      # select successes
        #print(sub)
        return(np.shape(sub)[0])
    
    def getRejects(self, data):
        sub = data[data[:,1] == self.getMe(data)]     # select my rows
        sub = sub[sub[:,4] == 0]                      # select successes
        return(np.shape(sub)[0])
    
    def getNumberOfOffers(self, data):
        sub = data[data[:,1] == self.getMe(data)]     # select my rows
        return(np.shape(sub)[0])
        
    def getMe(self, data):
        if data.size > 0:
            return(float(data[0,1]))
        else: 
            return(0)
