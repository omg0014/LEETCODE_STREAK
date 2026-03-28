class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=str(n)
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        arr=[]
        minn=min(d.values())
        for i,j in d.items():
            if j==minn:
                arr.append(int(i))
        return min(arr)
        