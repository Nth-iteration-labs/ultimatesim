# -*- coding: utf-8 -*-
from policies.responsePolicy import responsePolicy
import numpy as np

class RANDOMResponse(responsePolicy):
    
    def __init__(self):
        self.name = "RANDOM"
     
        
    def doResponse(self, offer, data, partner, prob=.5):

        return(int(np.random.binomial(1, prob, 1)))
        

    # -*- coding: utf-8 -*-

