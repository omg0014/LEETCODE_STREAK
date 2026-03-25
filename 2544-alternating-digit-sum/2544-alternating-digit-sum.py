class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        c=0
        for i in range(len(s)):
            if i%2==0:
                c+=int(s[i])
            else:
                c-=int(s[i])
        return c

        