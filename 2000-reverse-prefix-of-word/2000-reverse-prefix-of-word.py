class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c=-1
        for i in range(len(word)):
            if word[i]==ch:
                c=i
                break
        if c==-1:
            return word
        elif c==len(word)-1:
            return word[::-1]
        else:
            return word[c::-1] + word[c+1:]
        