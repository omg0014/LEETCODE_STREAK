class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=list(set(nums))
        while nums:
            nums.pop()
        for i in a:
            nums.append(i)
        nums.sort()
        