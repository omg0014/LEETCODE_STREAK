class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=1
        for i in nums:
            if i!=0:
                x*=i
        a=nums.count(0)
        if a>1:
            arr=[0]*(len(nums))
            return arr
        y=-1
        for i in range(len(nums)):
            if nums[i]==0:
                y=i
        lst=[]
        for i in range (len(nums)):
            if y==i:
                lst.append(x)
            elif a==1:
                lst.append(0)
            else:
                lst.append(x//nums[i])
        return lst 

        