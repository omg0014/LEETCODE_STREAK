class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        lst=[]
        for i,j in points:
            if x==i or y==j:
                a=abs(x-i)+abs(y-j)
                lst.append(a)
            else:
                lst.append(float("inf"))
        m= min(lst)
        if m==float("inf"):
            return -1
        for i in range(len(lst)):
            if lst[i]==m:
                return i

        