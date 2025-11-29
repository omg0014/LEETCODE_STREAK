class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        summ=sum(nums)
        c=0
        while summ%k!=0:
            summ-=1
            c+=1
        return c

        