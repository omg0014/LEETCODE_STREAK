class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        lst=[[]for i in range(m)]
        if len(original) != m * n:
            return []
        c=0
        for i in range(m):
            for j in range(n):
                lst[i].append(original[c])
                c+=1
        return (lst)
        