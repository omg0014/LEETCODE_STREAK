class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        arr=list(d.values())
        arr.sort()
        c=0
        for i in range(len(arr)-k):
            c+=arr[i]
        return c

        