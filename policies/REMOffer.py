# -*- coding: utf-8 -*-
from policies.offerPolicy import offerPolicy

class REMOffer(offerPolicy):
    
    def __init__(self):
        offerPolicy.__init__(self)
        self.name = "REM"
    
    # The rational economic man should always play a bid of 1
    def doOffer(self, data, partner):
        return(1)