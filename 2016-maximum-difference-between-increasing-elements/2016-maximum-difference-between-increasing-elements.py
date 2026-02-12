class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff=-1
        x=nums[0]
        for i in range(1,len(nums)):
            a=nums[i-1]
            a=min(x,a)
            x=a
            b=nums[i]
            if a<b:
                diff=max(b-a,diff)
        return diff

        