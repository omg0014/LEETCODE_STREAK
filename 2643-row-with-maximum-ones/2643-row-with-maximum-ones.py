class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        c=0
        ind=-1
        maxx=-1
        for i in mat:
            a=i.count(1)
            if a>maxx:
                ind=c
                maxx=a
            c+=1
        return [ind,maxx]



        