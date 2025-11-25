class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        x=-1
        y=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                x=mid
                r=mid-1 
            elif  nums[mid]<target  :
                l=mid+1
            else:
                r=mid-1  
        a=0
        b=len(nums)-1
        while a<=b:
            mid=(a+b)//2
            if nums[mid]==target:
                y=mid
                a=mid+1 
            elif  nums[mid]<target  :
                a=mid+1
            else:
                b=mid-1
        return [x,y]  