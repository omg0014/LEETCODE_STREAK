class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i,j in d.items():
            if j%k==0:
                c+=i*j
        return c
