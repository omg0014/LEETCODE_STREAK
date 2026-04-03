class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        a=-1
        b=-1
        res=float("inf")
        for i in range(len(nums)):
            if nums[i]==1:
                a=i
                if b!=-1:
                    res=min(abs(a-b),res)
            if nums[i]==2:
                b=i
                if a!=-1:
                    res=min(abs(a-b),res)
        if res==float("inf"):
            return -1
        return res
        