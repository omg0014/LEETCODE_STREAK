class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        x=sorted(set(nums1))
        y=sorted(set(nums2))
        d={}
        for i in x:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in y:
            if i in d:
                return i
        return -1

        