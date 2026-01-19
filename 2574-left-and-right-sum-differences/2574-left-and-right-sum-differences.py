class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        c=0
        n=len(nums)
        for i in nums:
            left.append(c)
            c+=i
        c=0
        for i in range(n-1,-1,-1):
            right.append(c)
            c+=nums[i]
        a=right[::-1]
        lst=[]
        for i in range(len(left)):
            lst.append(abs(a[i]-left[i]))
        return lst

        