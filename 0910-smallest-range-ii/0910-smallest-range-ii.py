class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]  

        for i in range(n - 1):
            maxx = max(nums[i] + k, nums[-1] - k)
            minn = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, maxx - minn)

        return ans
            