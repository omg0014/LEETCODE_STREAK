class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        l=0
        r=1
        lst=[]
        c=1
        while r<len(nums):
            a=nums[l]
            b=nums[r]
            if a<b:
                c+=1
            else:
                lst.append(c)
                c=1
            l+=1
            r+=1
        lst.append(c)
        return max(lst)
        


        