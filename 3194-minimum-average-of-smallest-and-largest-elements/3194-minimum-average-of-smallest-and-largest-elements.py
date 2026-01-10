class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        lst=[]
        l=0
        r=len(nums)-1
        while l<r:
            a=nums[l]
            b=nums[r]
            c=(a+b)/2
            lst.append(c)
            l+=1
            r-=1
        return min(lst)

        