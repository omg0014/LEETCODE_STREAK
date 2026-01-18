class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d={}
        arr=[]
        for i in range(1,len(nums)+1):
            d[i]=0
        for i in nums:
            d[i]+=1
        for i,j in d.items():
            if j==0:
                arr.append(i)
        return arr

