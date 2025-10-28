class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=""
        for i,j in d.items():
            if j==1:
                x+=i
                break
        for i in range(len(s)):
            if s[i]==x:
                return i
        return -1

        