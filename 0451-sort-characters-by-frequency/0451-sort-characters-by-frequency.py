class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=""
        data = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        for i,j in data.items():
            for _ in range(j):
                s+=i
        # for i in range(len(s)):
        #     s[i]=new[i]
        return s

        # lst=[d.values()]
        # new=(list(set(lst)))
        
        