class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lst=[]
        for i in range(len(arr)+k):
            if i+1 not in arr:
                lst.append(i+1)
        return lst[k-1]

        