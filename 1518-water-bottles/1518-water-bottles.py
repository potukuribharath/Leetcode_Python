class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        tot=numBottles
        
        while True:
            exi=int(numBottles/numExchange)
            
            rem=int(numBottles%numExchange)
            
           
            
            tot+=exi
            numBottles=rem+exi
            if exi+rem < numExchange:
                break
                
        
                
        return int(tot)