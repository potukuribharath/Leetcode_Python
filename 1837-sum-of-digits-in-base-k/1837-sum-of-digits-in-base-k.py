class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num=n//k+n%k
        s=0
        while n>0:
            s+=n%k
            n=n//k
        return s
            
        