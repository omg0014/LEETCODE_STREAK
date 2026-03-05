class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x=True
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                x=False
        a=True
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                a=False
        if a==True or x==True:
            return True
        else:
            return False
        
        
        