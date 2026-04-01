class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))
        d={}
        for i in nums1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums2:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums3:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        arr=[]
        for i,j in d.items():
            if j>=2:
                arr.append(i)
        return arr

        