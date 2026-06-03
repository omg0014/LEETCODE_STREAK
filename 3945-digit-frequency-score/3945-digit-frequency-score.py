class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=str(n)
        total=0
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            total+=int(i)*j
        return total
            

        