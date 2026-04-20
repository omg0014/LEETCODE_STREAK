class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist=0
        n=len(colors)
        for i in range(n):
            if colors[i]!=colors[n-1]:
                max_dist=abs(i-(n-1))
                break
        maxx=0
        for j in range(n-1,-1,-1):
            if colors[j]!=colors[0]:
                maxx=j
                break
        print(maxx,max_dist)
        return max(maxx,max_dist)
