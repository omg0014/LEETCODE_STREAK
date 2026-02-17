class Solution:
    def secondHighest(self, s: str) -> int:
        lst=[]
        for i in s:
            if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i =="7" or i == "8" or i == "9" or i=="0":
                lst.append(int(i))
        l=set(lst)
        a=list(l)
        a.sort()
        if len(a)<2:
            return -1
        else:
            return a[-2]
        