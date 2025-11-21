class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        arr=[]
        for i in nums:
            lst.append(i)
        lst.sort()
        for i in range(len(nums)):
            c=0
            for j in range(len(lst)):
                if nums[i]>nums[j]:
                    c+=1
            arr.append(c)
        return arr
        