class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        lst=heights.copy()
        lst.sort()
        c=0
        for i in range(len(lst)):
            if lst[i]!=heights[i]:
                c+=1
        return c
        