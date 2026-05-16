class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        arr=nums[::-1]
        return nums+arr
        