class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=nums1
        b=(nums2)
        d={}
        arr=[]
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in b:
            if i in d and d[i]>0:
                d[i]-=1
                arr.append(i)
        return arr       