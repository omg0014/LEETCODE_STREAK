class Solution:
    def reverseVowels(self, s: str) -> str:
        f=s.lower()
        x=[]
        lst=list(s)
        for i in range(len(s)):
            if f[i]=="a" or f[i]=="e" or f[i]=="i" or f[i]=="o" or f[i]=="u":
                x.append(i)
        if len(x)==1 or len(x)==0:
            return s
        l=0
        r=len(x)-1
        while l<r:
            lst[x[l]],lst[x[r]]=lst[x[r]],lst[x[l]]
            l+=1
            r-=1
        w= "".join(lst)
        return w
        