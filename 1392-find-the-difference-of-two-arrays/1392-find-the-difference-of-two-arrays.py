class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=set(nums1)
        b=set(nums2)
        x=[]
        arr1=[]
        arr2=[]
        for i in a:
            if i not in b:
                arr1.append(i)
        for i in b:
            if i not in a:
                arr2.append(i)
        x.append(arr1)
        x.append(arr2)
        return x

        

        