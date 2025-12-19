class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        c=0
        for i in  range(0,n,2):
            c+=nums[i]
        return c
        