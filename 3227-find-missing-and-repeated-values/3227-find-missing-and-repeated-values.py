class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a=len(grid)
        l=[]
        arr=[]
        for i in range(a):
            for j in range(a):
                if grid[i][j] not in l:
                    l.append(grid[i][j])
                else:
                    arr.append(grid[i][j])
        l.sort()
        # d={}
        # for i in l:
        #     if i in d:
        #         arr.append(i)
        #     else:
        #         d[i]=1
        x=len(l)+1
        for i in range(len(l)):
            if l[i]!=i+1:
                x=i+1
                break
        arr.append(x)
        
        return arr
