class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=sorted(nums1)
        for i in nums1:
            if i in nums2:
                return i
        s="" 
        s=str(min(nums1))+str(min(nums2))
        n=int(s[-1]+s[-2])
        s=int(s)
        if s<n:
            return s
        else:
            return n
        
        