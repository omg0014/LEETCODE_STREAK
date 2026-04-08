class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        con=[0]
        vowel=[0]
        for i,j in d.items():
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                con.append(j)
            else:
                vowel.append(j)
        return max(con)+max(vowel)

        

        