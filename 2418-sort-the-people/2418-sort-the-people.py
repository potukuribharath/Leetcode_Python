class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={}
        for i in range(0,len(heights)):
            dic[i]=heights[i]
        s=sorted(dic.values(),reverse=True)
        li=[]
        for i in s:
            li.append(names[list(dic.keys())[list(dic.values()).index(i)]])
        
        return li
        