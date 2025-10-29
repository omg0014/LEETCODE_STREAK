class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=[]
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j==1:
                arr.append(i)
            if j>=2:
                arr.append(i)
                arr.append(i)
        x=len(nums)-len(arr)
        for i in range(x):
            nums.pop()
        for i in range(len(arr)):
            nums[i]=arr[i]
            

        