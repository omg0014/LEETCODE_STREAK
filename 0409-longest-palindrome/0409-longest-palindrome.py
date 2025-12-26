class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for j,i in d.items():
            if i%2==0:
                c+=i
            elif i>2:
                x=i-1
                c+=x
                d[j]-=x
        for i in d.values():
            if i==1:
                c+=1
                break
        return c
        