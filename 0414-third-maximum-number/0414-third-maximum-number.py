class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=list(set(nums))
        s.sort()
        # nums.sort()
        if len(s)<3:
            return s[-1]
        return s[-3]
        