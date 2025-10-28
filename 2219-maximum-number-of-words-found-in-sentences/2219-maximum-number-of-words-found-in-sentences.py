class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        for i in sentences:
            x=1
            for j in i:
                if j==" ":
                    x+=1
            c=max(c,x)
        return c
        

        