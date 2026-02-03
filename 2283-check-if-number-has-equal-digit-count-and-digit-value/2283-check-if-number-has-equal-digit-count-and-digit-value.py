class Solution:
    def digitCount(self, num: str) -> bool:
        d={}
        for i in range(len(num)):
            d[i]=0

        for i in num:
            a=int(i)
            if a in d:
                d[a]+=1
            else:
                d[a]=1

        for i in range(len(num)):
            a=int(num[i])
            if d[i]!=a:
                return False
        return True
        