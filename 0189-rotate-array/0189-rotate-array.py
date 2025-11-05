from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dq=deque(nums)
        for i in range(k):
            x=dq.pop()
            dq.appendleft(x)
        for i in range(len(nums)):
            nums[i]=dq[i]
        return nums


