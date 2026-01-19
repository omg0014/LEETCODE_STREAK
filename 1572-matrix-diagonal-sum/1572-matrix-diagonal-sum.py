class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        c=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    c+=mat[i][j]
                elif i+j==n-1:
                    c+=mat[i][j]
        return c
        