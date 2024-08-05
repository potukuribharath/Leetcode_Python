class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        li=[]
        cou=0
        for i in arr:
            if arr.count(i)==1:
                li.append(i)
                cou+=1
                if cou==k:
                    return li[k-1]
        return ""
        
                