class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        l=0
        r=1
        while r<len(s):
            if abs((int(s[l])-int(s[r])))>2:
                return False
            l+=1
            r+=1
        return True
        