# https://leetcode.com/problems/loud-and-rich/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        @cache
        def dfs(u):
            ans[u] = u
            for v in graph[u]:
                candidate = dfs(v)
                if quiet[candidate] < quiet[ans[u]]:
                    ans[u] = candidate
            
            return ans[u]
        
        n = len(quiet)
        graph = defaultdict(lambda: [])
        for (u, v) in richer: 
            graph[v].append(u)
            
        ans = [None for _ in range(n)]
        
        for i in range(n):
            ans[i] = dfs(i)
            
        return ans
        
class Solution2:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(u):
            ans = (quiet[u], u)
            stack = [u]
            seen = {u: True}
            while stack: 
                u = stack.pop()
                for v in graph[u]:
                    if v not in seen: 
                        seen[v] = True
                        ans = min(ans, (quiet[v], v))
                        stack.append(v)
                    
            return ans[1]
                    
        
        n = len(quiet)
        graph = defaultdict(lambda: [])
        for (u, v) in richer: 
            graph[v].append(u)
            
        ans = [None for _ in range(n)]
        
        for i in range(n):
            ans[i] = dfs(i)
            
        return ans
        
        
        
        
        
        
        
        
