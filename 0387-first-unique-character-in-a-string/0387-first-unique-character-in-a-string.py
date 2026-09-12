class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range (len(s)):
            a=s[i]
            if d[a]==1:
                return i
        return -1
        