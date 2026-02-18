class Solution:
    def findGCD(self, nums):
        s = min(nums)   
        l = max(nums) 
        
        while s != 0:
            s, l = l % s, s
        
        return l

        