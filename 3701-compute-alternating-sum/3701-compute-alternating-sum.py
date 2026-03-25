class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        c=0
        e=0
        for i in range(len(nums)):
            if i%2==0:
                c+=nums[i]
            else:
                e+=nums[i]      
        return c-e  