class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[]for _ in range(n)]
        visited=[0 for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node,x):
            visited[node]=1
            x.append(node)
            for i in adj[node]:
                if visited[i]==0:
                    dfs(i,x)
        ans=[]
        for i in range(n):
            if visited[i]==0:
                x=[]
                dfs(i,x)
                ans.append(x)
        for i in ans:
            if source in i and destination in i:
                return True
        return False
            
        
        