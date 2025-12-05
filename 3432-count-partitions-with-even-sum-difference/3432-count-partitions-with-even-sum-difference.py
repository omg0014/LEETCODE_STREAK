class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        summ=sum(nums)
        c=0
        x=0
        for i in range(len(nums)-1):
            c+=nums[i]
            rem=summ-c
            if (c-rem)%2==0:
                x+=1
        return x

        