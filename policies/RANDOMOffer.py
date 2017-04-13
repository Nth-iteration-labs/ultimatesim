# -*- coding: utf-8 -*-
from policies.offerPolicy import offerPolicy
import numpy as np

class RANDOMOffer(offerPolicy):
    
    def __init__(self):
        offerPolicy.__init__(self)
        self.name = "RANDOM"
    
    # The rational economic man should always play a bid of 1
    def doOffer(self, data, partner):
        return(float(np.random.randint(11, size=1)))# -*- coding: utf-8 -*-

