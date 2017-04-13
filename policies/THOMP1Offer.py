# -*- coding: utf-8 -*-
from policies.offerPolicy import offerPolicy

class REMOffer(offerPolicy):
    
    def __init__(self):
        offerPolicy.__init__(self)
        self.name = "REM"
    
    # The rational economic man should always play a bid of 1
    def doOffer(self, data, partner):
        
        # Get success and failures for each offer 0-10
        # a = self.getSuccesPerOffer(data)
        # b = self.getFailurePerOffer(data)
        
        # Contruct beta posterior
        # max = 0
        # choice = 0
        # for(i in range(10)):
            #draw = rbeta(1, a[i]+1, b[i]+1)
            #if draw > max:
                # max = draw
                # choice = i
        # return (choice)
        return(1)