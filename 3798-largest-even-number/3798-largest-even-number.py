class Solution:
    def largestEven(self, s: str) -> str:
        lst=[]
        for i in s:
            lst.append(i)
        for i in range(len(s)-1,-1,-1):
            if lst[i]=="2":
                break
            else:
                lst[i]=""
        a="".join(lst)
        if len(a)==0:
            return ""
        b=int(a)
        c=str(b)
        return c
        