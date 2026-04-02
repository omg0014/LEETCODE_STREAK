class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i in d and i%2==0:
                d[i]+=1
            else:
                d[i]=1
        for i in nums:
            if i%2==0 and d[i]==1:
                return i
        return -1
        