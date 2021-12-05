# https://leetcode.com/problems/valid-arrangement-of-pairs/

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        def dfs(u):
            while adj[u]:
                v = adj[u].pop()
                dfs(v)                
                ans.append([u, v])
                            
        adj = defaultdict(lambda: [])
        degree = defaultdict(lambda: 0)
        
        for (u, v) in pairs: 
            adj[u].append(v)
            degree[u] += 1
            degree[v] -= 1
            
        start = pairs[0][0]
        for u in adj: 
            if degree[u] == 1: 
                start = u
                break
           
        ans = []
        
        dfs(start)
        
        return ans[::-1]
