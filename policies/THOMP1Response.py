# -*- coding: utf-8 -*-
from policies.responsePolicy import responsePolicy
import numpy as np

class REMResponse(responsePolicy):
    
    def __init__(self):
        self.name = "REM"
        
    def doResponse(self, offer, data, partner):
        
        # Get succesfull accepts (no of accepts)
        # Get succesfull reject (0)
        # Get total number of responses
        
        # d1 = rbeta(1, )
        # d2 = rbeta(1, )
        
        # response = d1>d2, 1, 0
        # return (response)
        
        return(1)
        

    