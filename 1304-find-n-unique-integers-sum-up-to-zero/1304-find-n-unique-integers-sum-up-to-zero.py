class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst=[]
        for i in range(n//2):
            lst.append(i+1)
            lst.append(-(i+1))
        if n%2!=0:
            lst.append(0)
        lst.sort()
        return lst


        