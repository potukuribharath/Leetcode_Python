class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n=sorted(nums)
        if n[-2]*2 <= n[-1]:
            return nums.index(n[-1])
        else:
            return -1
        