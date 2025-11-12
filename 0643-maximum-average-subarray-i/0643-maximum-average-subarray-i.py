class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c=0
        lst=[]
        x=0
        y=0
        for i in nums:
            c+=i
            x+=1
            if x>=k:
                lst.append(c)
                c-=nums[y]
                y+=1
        arr=[]
        for i in lst:
            arr.append(i/k)
        return max(arr)



        