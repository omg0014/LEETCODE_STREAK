class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r and r<len(nums):
            mid=(l+r)//2
            x=nums[mid]
            if target<x:
                r=mid-1
            elif target==x:
                return mid
            else:
                l=mid+1
        return -1
        