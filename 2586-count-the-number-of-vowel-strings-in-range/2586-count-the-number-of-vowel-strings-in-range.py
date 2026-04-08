class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            a=words[i]
            if (a[0]=="a" or a[0]=="e" or a[0]=="i" or a[0]=="o" or a[0]=="u")and(a[-1]=="a" or a[-1]=="e" or a[-1]=="i" or a[-1]=="o" or a[-1]=="u"):
                c+=1
        return c