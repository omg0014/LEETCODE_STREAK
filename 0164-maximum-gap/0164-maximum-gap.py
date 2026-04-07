class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # if len(nums)<0:
        #     return 0
        nums.sort()
        minn=0
        for i in range(1,len(nums)):
            minn=max(minn,(nums[i]-nums[i-1]))
        return minn        