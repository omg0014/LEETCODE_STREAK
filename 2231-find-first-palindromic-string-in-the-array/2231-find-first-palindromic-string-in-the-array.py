class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            x=i[::-1]
            if x==i:
                return i
        return ""
        