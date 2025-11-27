class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        a=list(s)
        n=len(a)
        c=0
        dp=[0 for i in range(n+1)]
        for i in range(len(a)):
            x=a[i]
            if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
                c+=1
                dp[i+1]=c
            else:
                dp[i+1]=c
        l=1
        r=k
        maxx=0
        while r<n+1:
            maxx=max(dp[r]-dp[l-1],maxx)
            l+=1
            r+=1
        return maxx


        