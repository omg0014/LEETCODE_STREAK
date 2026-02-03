class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m=max(d.values())
        lst=[0 for _ in range(m+1)]
        lst[0]=1
        lst[1]=1
        for i in range(2,m+1):
            for j in range(i*i,m+1,i):
                lst[j]=1
        # print(lst)
        for i in d.values():
            if lst[i]==0:
                return True
        return False

        