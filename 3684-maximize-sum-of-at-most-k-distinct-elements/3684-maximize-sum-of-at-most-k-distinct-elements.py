class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=list(set(nums))
        s.sort(reverse=True)
        lst=[]
        if k>len(s):
            k=len(s)
        for i in range(k):
            lst.append(s[i])
        return lst


        