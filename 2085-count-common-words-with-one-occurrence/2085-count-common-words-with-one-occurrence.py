class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d={}
        for i in words1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        lst=[]
        for i,j in d.items():
            if j==1:
                lst.append(i)
        d1={}
        for i in words2:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        arr=[]
        for i,j in d1.items():
            if j==1:
                arr.append(i)
        c=0
        for i in lst:
            if i in arr:
                c+=1
        return c
        
        
        