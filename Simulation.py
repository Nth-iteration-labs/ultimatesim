# -*- coding: utf-8 -*-
from Population import Population
import numpy as np
from matplotlib import pyplot as pl

class Simulation:
    """ Class for running a large number of simulations
    """
    
    def __init__(self, size, name="None"):
        self.nsims = size
        self.name = name
        
        self.data = np.empty([0,4])
        
        self.rounds = 0
        self.popSize = 0
        self.offers = []
        self.responses = []
        self.probs = []
        self.storeall = False
        self.data = np.empty(size, dtype=np.matrix)
        
    def Initialize(self, rounds, popSize, offers, responses, probs, storeall=False):
        print("Initialize")
        
        self.rounds = rounds
        self.popSize = popSize
        self.offers = offers
        self.responses = responses
        self.probs=probs
        #print(probs)
        if storeall:
            self.storeall = storeall
            self.populations = np.empty(self.nsims, dtype=object)
                
              
        
    def Run(self, verbose=False, save=False):
        
        for i in range(self.nsims):
        
            if verbose:
                print("Now running simulation: ",(i+1))
            
            population = Population(self.popSize)
            population.populate(self.offers, self.responses, self.probs)
            population.play(self.rounds)
            
            # Retain all populations in memory
            # Not yet implemented
            #if self.storeall:
                #self.populations[i] = population    
            
            self.data[i] = population.getData()
            
        if self.storeall:
            name = "Sim_"+str(self.name)+"_r"+str(self.rounds)+"_p"+str(self.popSize) 
            print("Storing data under name: "+name)
            for i in range(self.nsims): 
                np.savetxt("data/"+name+"("+str(i)+").csv", self.data[i], delimiter=",")
                #print(self.data[i])
   
    
    def printData(self):
        print(self.data)

     
    def plotAverageBid(self):
        
        x = np.arange(self.rounds)
        y = np.empty(self.rounds, dtype=float)
        err = np.empty(self.rounds, dtype=float)
        
        for i in range(self.rounds):
            m = 0
            v = 0
            for j in range(self.nsims):
                m += self.data[j][i,1]
                v += (self.data[j][i,2] / np.sqrt(self.popSize))
            m = m / self.nsims
            v = v / self.nsims
            y[i] = m
            err[i] = v
        
        self.plotLines(x, y, err, "Average offer per round")
       
        
    def plotAverageProfit(self):
        
        x = np.arange(self.rounds)
        y = np.empty(self.rounds, dtype=float)
        err = np.empty(self.rounds, dtype=float)
        
        for i in range(self.rounds):
            m = 0
            v = 0
            for j in range(self.nsims):
                m += self.data[j][i,3]
                v += (self.data[j][i,4] / np.sqrt(self.popSize))
            m = m / self.nsims
            v = v / self.nsims
            y[i] = m
            err[i] = v
        
        self.plotLines(x, y, err, "Average profit per round")
    
    def plotAverageResponse(self):
        
        x = np.arange(self.rounds)
        y = np.empty(self.rounds, dtype=float)
        #err = np.empty(self.rounds, dtype=float)
        
        for i in range(self.rounds):
            m = 0
            for j in range(self.nsims):
                m += self.data[j][i,5]
            m = m / self.nsims
            y[i] = m
        
        pl.plot(x, y, 'k-')
        pl.ylim([0,1])
        pl.title("Average response per round")
        pl.show()
        
    
    def plotLines(self, x, y, err, name="None"):

        pl.plot(x,y, 'k-')
        pl.title(name)
        pl.ylim([0,10])
        pl.fill_between(x, y+err, y-err)
        pl.show()
