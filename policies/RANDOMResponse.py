# -*- coding: utf-8 -*-
from policies.responsePolicy import responsePolicy
import numpy as np

class RANDOMResponse(responsePolicy):
    
    def __init__(self):
        self.name = "RANDOM"
     
        
    def doResponse(self, offer, data, partner):

        return(int(np.random.binomial(1, .5, 1)))
        

    # -*- coding: utf-8 -*-

