class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        new=[]
        for i in range(len(odd)):
            new.append(even[i])
            new.append(odd[i])
        if len(odd)!=len(even):
            new.append(even[-1])
        for i in range(len(new)):
            nums[i]=new[i]
        return nums
