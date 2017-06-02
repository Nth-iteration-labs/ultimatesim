# -*- coding: utf-8 -*-
from policies.offerPolicy import offerPolicy
import numpy as np

class THOMP1Offer(offerPolicy):
    
    def __init__(self):
        offerPolicy.__init__(self)
        self.name = "REM"
    
    # The rational economic man should always play a bid of 1
    def doOffer(self, data, partner):
        
        # Get success and failures for each offer 0-10
        a = self.getSuccesPerOffer(data)
        b = self.getFailuresPerOffer(data)
        
        # Contruct beta posterior
        max = 0
        choice = 0
        for i in range(a.size) :
            draw = np.random.beta(a[i]+1, b[i]+1, 1) * i
            if draw > max:
                max = draw
                choice = i
        return (choice)