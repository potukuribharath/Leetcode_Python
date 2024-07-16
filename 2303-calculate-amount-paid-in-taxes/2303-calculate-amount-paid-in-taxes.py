class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income==0:
            return 0
        else:
            
            tax=0
            if len(brackets)==1:
                tax+=income*(brackets[0][1])/100
                return tax
            if income>brackets[0][0]:
                tax+=brackets[0][0]*(brackets[0][1])/100
                income-=brackets[0][0]
            else:
                tax+=income*(brackets[0][1])/100
                return tax
    
            for i in range(1,len(brackets)):
                
                if income > 0:
                    if income>=brackets[i][0]-brackets[i-1][0]:
                        rem=brackets[i][0]-brackets[i-1][0]
                        tax+=rem*(brackets[i][1])/100
                        income-=rem
                       

                    else:
                        tax+=income*(brackets[i][1])/100
                        break
                        
            return tax
        