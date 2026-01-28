class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}

      
        for i in grid:
            a = ",".join(map(str, i))   
            if a in d:
                d[a] += 1
            else:
                d[a] = 1

        c = 0


        for i in range(len(grid)):
            arr = []
            for j in range(len(grid)):
                arr.append(grid[j][i])

            s = ",".join(map(str, arr))  
            if s in d:
                c += d[s]  

        return c
