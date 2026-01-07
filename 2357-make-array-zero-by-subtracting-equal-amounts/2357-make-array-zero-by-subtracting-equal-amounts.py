class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=list(set(nums))
        zero=s.count(0)
        return len(s)-zero
        