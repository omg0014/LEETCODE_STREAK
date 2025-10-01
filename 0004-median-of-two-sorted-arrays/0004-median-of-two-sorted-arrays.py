class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if len(nums1)%2==0:
            a=len(nums1)//2
            b=(len(nums1)//2)-1
            return (nums1[a]+nums1[b])/2
        else:
            a=len(nums1)//2
            return nums1[a]
        