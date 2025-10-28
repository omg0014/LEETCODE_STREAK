class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=[]
        for i in range(m):
            arr.append(nums1[i])
        for i in range(n):
            arr.append(nums2[i])
        arr.sort()
        for i in range(len(arr)):
            nums1[i] = arr[i]