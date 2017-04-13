# -*- coding: utf-8 -*-
class responsePolicy:
    """ Baseline policy """
    
    def __init__(self):
        self.name = "None"
     
    def doResponse(self, offer, data, partner):
        print("WARNING: DEFAULT RESPONSE")
        return(0)
    
    def printData(self, data):
        print(data)
        

