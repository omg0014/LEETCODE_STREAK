class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        arr=[]
        d={}
        for i in nums:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        for i,j in d.items():
            if j==n:
                arr.append(i)
        arr.sort()
        return arr

        