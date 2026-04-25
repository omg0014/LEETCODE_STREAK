class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            a=str(i)
            if len(a)%2==0:
                c+=1
        return c
        