class Solution:
    def largestOddNumber(self, num: str) -> str:

        # l=[]
        # for i in num:
        #     l.append(i)
        # for i in range(len(num)-1,-1,-1):
        #     if int(l[i])%2==0:
        #         l[i]=""
        #     else:
        #         break
        # s="".join(l)
        # if len(s)==0:
        #     return ""
        # # print(s)
        # x=int(s)
        # return (str(x))

        lst=[]
        for i in num:
            lst.append(i)
        for i in range(len(lst)-1,-1,-1):
            if int(lst[i])%2==0:
                lst[i]=""
            else:
                break
        # print(lst)
        a="".join(lst)
        if len(a)==0:
            return ""
        # b=int(a)
        # c=str(b)
        return a
        
        