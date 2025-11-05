class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=list(d.values())
        s=list(set(x))
        if len(x)==len(s):
            return True
        else:
            return False
        