class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        m=max(nums)
        l=[0]*(m+1)
        l[0]=l[1]=1
        for i in range(2,m+1):
            for j in range(i*i,m+1,i):
                l[j]=1
        lst=[]
        for i in range (len(nums)) :
            if l[nums[i]]==0:
                lst.append(i)
        return abs(lst[0]-lst[-1])
        