class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        x=False
        for i in range (len(nums)):
            if nums[i]==target:
                x=True
        return x
        
        