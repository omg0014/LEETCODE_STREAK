class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        # neg=0
        # pos=0
        # c=0
        # for i in nums:
        #     if i>0:
        #         pos+=1
        #     else:
        #         neg+=1
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]=-nums[i]
                k-=1
        nums.sort()
        if k%2==0:
            k=0
        else:
            k=1
        if k==1:
            nums[0]=-nums[0]
        print(nums)
        return sum(nums)

        