class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst=[]
        x=0
        y=0
        c=0
        while x<len(word1) and y<len(word2):
            if c%2==0:
                lst.append(word1[x])
                x+=1
            else:
                lst.append(word2[y])
                y+=1
            c+=1
        while x<len(word1):
            lst.append(word1[x])
            x+=1
        while y<len(word2):
            lst.append(word2[y])
            y+=1
        s="".join(lst)
        return s
        


        