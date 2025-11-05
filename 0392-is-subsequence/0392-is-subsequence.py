class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        l=0
        r=0
        while r<len(t) and l<len(s):
            if s[l]==t[r]:
                l+=1
            r+=1
        if l==len(s):
            return True
        else:
            return False
        