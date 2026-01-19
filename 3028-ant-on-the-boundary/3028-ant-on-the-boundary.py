class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c=0
        x=0
        for i in nums:
            c+=i
            if c==0:
                x+=1
        return x
        