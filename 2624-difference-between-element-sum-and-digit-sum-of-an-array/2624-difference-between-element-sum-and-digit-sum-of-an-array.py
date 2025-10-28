class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        summ=sum(nums)
        x=0
        for i in nums:
            s=str(i)
            for j in s:
                x+=int(j)
        return abs(summ-x)

        