class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        a=grid[0]

        for i in grid:
            if i != a:

                return False

        for i in range(1,len(a)):
            if a[i-1]==a[i]:
    
                return False
        return True


        