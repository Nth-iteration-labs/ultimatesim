# -*- coding: utf-8 -*-
from policies.responsePolicy import responsePolicy
import numpy as np

class RADNOMResponse(responsePolicy):
    
    def __init__(self):
        self.name = "RANDOM"
        
    def doResponse(self, offer, data, partner):
        
        if(offer>0):
            return(1)
        else:
            return(int(np.random.binomial(1, .5, 1)))
        

    # -*- coding: utf-8 -*-

