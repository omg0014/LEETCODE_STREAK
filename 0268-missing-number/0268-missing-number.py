class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        x=len(nums)
        for i in range(len(nums)):
            if nums[i]!=i:
                x=i
                break
        return x

        