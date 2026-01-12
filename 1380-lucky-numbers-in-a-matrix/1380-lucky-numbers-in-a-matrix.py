class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minn=[]
        for i in matrix:
            minn.append(min(i))
        maxx=[]
        for i in range(len(matrix[0])):
            lst=[]
            for j in range(len(matrix)):
                lst.append(matrix[j][i])
            maxx.append(max(lst))
        for i in minn :
            if i in maxx:
                return [i]
        return []

                