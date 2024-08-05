class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s=""
        li=[]
        for i in arr:
            if arr.count(i)>1:
                continue
            else:
                print(i)
                li.append(i)
        if len(li)<k:
            return ""
        else:
            return li[k-1]
                