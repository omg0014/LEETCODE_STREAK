class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i,j in d.items():
            if j==1:
                c+=i
        return c
        