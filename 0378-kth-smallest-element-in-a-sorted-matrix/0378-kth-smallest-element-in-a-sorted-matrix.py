class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst=[]
        a=len(matrix)
        b=len(matrix[0])
        for i in range(a):
            for j in range(b):
                lst.append(matrix[i][j])
        lst.sort()
        return lst[k-1]
        