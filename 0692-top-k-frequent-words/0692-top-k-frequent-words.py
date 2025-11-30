class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_dict = dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))

        lst=[]
        for i,j in sorted_dict.items():
            lst.append(i)
        return lst[:k]
        # return sorted_dict
        
        