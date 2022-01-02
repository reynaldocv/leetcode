# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:   
        def helper(u):
            visited[u] = True
            stack = [u]
            ans = -1
            while stack:
                newStack = []                                
                ans += 1
                for u in stack:                    
                    for v in graph[u]:
                        visited[v] = True
                        newStack.append(v)

                stack = newStack
            
            return ans
        
        bestFriends = []
        graph = defaultdict(lambda:[])
        
        for (i, fav) in enumerate(favorite):
            if i == favorite[fav]:
                if i < fav:
                    bestFriends.append((i, fav))
            else: 
                graph[fav].append(i)
            
        visited = {}
        ans = 0
        for (u, v) in bestFriends:  
            ans += helper(u) + 2 + helper(v)
            
        n = len(favorite)
        
        for i in range(n):
            if i not in visited: 
                seen = {}
                u = i
                cnt = 0
                while u not in seen: 
                    visited[u] = seen[u] = True
                    seen[u] = cnt
                    cnt += 1
                    u = favorite[u]
                    
                ans = max(ans, cnt - seen[u])
                
        return ans
                
