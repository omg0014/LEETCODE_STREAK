class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr=0
        maxx=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr+=1
                maxx=max(curr,maxx)
            else:
                curr=0
        return maxx
        