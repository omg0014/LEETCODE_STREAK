class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lst=[]
        for i in range(len(words)):
            for j in words[i]:
                if j==x:
                    lst.append(i)
                    break
        return lst


        