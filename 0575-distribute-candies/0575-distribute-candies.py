class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        l=len(list(set(candyType)))
        return min(l,len(candyType)//2)
        