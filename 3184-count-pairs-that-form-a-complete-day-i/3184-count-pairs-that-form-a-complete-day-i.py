class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d={}
        for i in hours:
            i=i%24
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in hours:
            i=i%24
            d[i]-=1
            a=24-i
            a=a%24
            if a in d:
                if d[a]>0:
                    c+=d[a]
        return c

        