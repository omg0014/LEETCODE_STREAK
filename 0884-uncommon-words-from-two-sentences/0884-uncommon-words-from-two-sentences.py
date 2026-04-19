class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        for i in s1.split():
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in s2.split():
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = []
        for i in d:
            if d[i] == 1:
                res.append(i)
        
        return res
        
        