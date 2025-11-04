class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        arr=[]
        for i in candies:
            if i+extraCandies>=m:
                arr.append(True)
            else:
                arr.append(False)
        return arr
        