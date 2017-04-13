# -*- coding: utf-8 -*-
class offerPolicy:
    """ Baseline policy """
    
    def __init__(self):
        self.name = "None"
    
    def doOffer(self, data, partner):
        print("WARNING: DEFAULT OFFER")
        return(0)
    
    
    def getSuccesPerOffer(self, data):
        """ Returns the number of successes for each offer in 0:10 """
        # Select succesful offers
        
        sub = data[data[:,2] == self.getMe(self.data)]     # select my rows
        sub = sub[sub[:,4] == 1]                            # select successes
         
        a = np.zeros(11)
        for i in range(a.size):
            a[i] = np.sum(sub[sub[:,3] == i][:,4])
        return(a)
    
    def getFailuresPerOffer(self, data):
        """ Returns the number of failures for each offer in 0:10 """
        # Select rejected offers
        # Group by size
        # Return
        
    def getMe(self, data):
        return(float(data[0,1]))



