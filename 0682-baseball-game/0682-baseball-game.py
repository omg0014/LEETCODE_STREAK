class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr=[]
        l=0
        while l<len(operations):
            a=operations[l]
            if a=="+" and len(arr)>=2:
                arr.append(arr[-1]+arr[-2])
            elif a=="C":
                arr.pop()
            elif a=="D":
                arr.append(2*arr[-1])
            else:
                arr.append(int(a))
            l+=1
        return sum(arr)

        