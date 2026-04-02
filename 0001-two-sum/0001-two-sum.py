class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=nums.copy()
        arr.sort()
        lst=[]
        l=0
        r=len(nums)-1
        while l<r:
            a=arr[l]
            b=arr[r]
            if a+b==target:
                lst.append(a)
                lst.append(b)
                l=r
            elif a+b>target:
                r-=1
            else:
                l+=1
        x,y=-1,-1
        for i in range(len(nums)):
            if nums[i]==lst[0] and x==-1:
                x=i
            elif  nums[i]==lst[1]:
                y=i
        return [x,y]



            
            

        

        