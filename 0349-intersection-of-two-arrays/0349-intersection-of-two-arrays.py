class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        d={}
        arr=[]
        for i in a:
            d[i]=1
        for i in b:
            if i in d:
                arr.append(i)
        return arr
        