# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def helper():
            stack = [0]
            seen = {0}
            
            ans = 1
            
            while stack: 
                newStack = []
                
                for u in stack: 
                    for v in graph[u]:
                        if v == n - 1: 
                            return ans 
                        
                        if v not in seen: 
                            seen.add(v)
                            
                            newStack.append(v)
                            
                stack = newStack
                ans += 1 
                
            return ans 
            
        graph = defaultdict(lambda: [])
        
        for i in range(n - 1):
            graph[i].append(i + 1)
            
        ans = []
            
        for (u, v) in queries: 
            graph[u].append(v)
            
            ans.append(helper())
            
        return ans 
            
        
