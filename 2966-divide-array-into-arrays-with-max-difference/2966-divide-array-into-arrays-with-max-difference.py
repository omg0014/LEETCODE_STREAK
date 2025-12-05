class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        arr=[]
        i=2
        while i<len(nums):
        # for i in range(2,len(nums)):
            a=nums[i-2]
            b=nums[i-1]
            c=nums[i]
            if abs(a-b)<=k and abs(a-c)<=k and abs(b-c)<=k:
                arr.append([a,b,c])
                i+=3
            else:
                return []
        return arr



        