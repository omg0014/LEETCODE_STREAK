class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if "" in strs:
            return ""
        arr=[]
        maxx_len=[]
        for i in strs:
            arr.append(len(i))
        minn=min(arr)
        n=len(strs)
        c=0
        maxx=""
        for i in range(minn):
            l=[]
            for j in strs:
                l.append(j[i])
            s=set(l)
            if len(s)==1:
                maxx+=l[0]
            else:
                maxx_len.append(maxx)
                maxx=""
                break
        maxx_len.append(maxx)
        # return maxx_len
        a=0
        for i in maxx_len:
            a=max(a,len(i))
        
        for i in maxx_len:
            if a==len(i):
                return i
        


            

                


        