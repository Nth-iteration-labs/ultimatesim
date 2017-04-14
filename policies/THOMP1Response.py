# -*- coding: utf-8 -*-
from policies.responsePolicy import responsePolicy
import numpy as np

class THOMP1Response(responsePolicy):
    
    def __init__(self):
        self.name = "REM"
        
    def doResponse(self, offer, data, partner):
        
        
        n = self.getNumberOfOffers(data)
        s = self.getAccepts(data)
        f = self.getRejects(data)
        
        #print("Successes: ",s," and failures", f)
        
        d1 = np.random.beta(s+1,1, 1)
        d2 = np.random.beta(1,f+1, 1)
        return (1 if d1>d2 else 0)


    