class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        x=""
        for i in range(len(s)):
            i=i+k
            i=i%len(s)
            x+=s[i]
        # for i in range(len(s)):
        #     s[i]=x[i]
        return x
        