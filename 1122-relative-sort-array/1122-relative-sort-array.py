class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst=[]
        d={}
        for i in arr1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in arr2:
            for j in range(d[i]):
                lst.append(i)
        arr1.sort()
        for i in arr1:
            if i not in arr2:
                lst.append(i)
        return lst


        