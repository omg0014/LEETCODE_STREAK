class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        lst=[]
        for i in range(n):
            for j in range(n):
                if i!=j and grid[i][j]==1:
                    lst.append(i)
        d={}
        for i in lst:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=max(d.values())
        for i,j in d.items():
            if j==x:
                return i


        