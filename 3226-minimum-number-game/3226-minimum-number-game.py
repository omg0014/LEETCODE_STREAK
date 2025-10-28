class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        l=0
        r=1
        while r<len(nums):
            arr.append(nums[r])       
            arr.append(nums[l]) 
            l+=2
            r+=2
        return arr