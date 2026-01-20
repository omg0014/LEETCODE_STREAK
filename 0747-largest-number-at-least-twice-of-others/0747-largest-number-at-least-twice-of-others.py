class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lst=[]
        for i in nums:
            lst.append(i)
            lst.sort()
        x=-1
        if lst[-1]>=2*lst[-2]:
            x=lst[-1]
        for i in range(len(nums)):
            if nums[i]==x:
                return i
        return -1

        