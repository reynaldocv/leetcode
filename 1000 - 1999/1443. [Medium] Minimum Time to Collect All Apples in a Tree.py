# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def helper(u):
            ans = 0 
            apples = False 
            
            for v in graph[u]:
                if v not in seen: 
                    seen.add(v)
                        
                    (apple, distance) = helper(v)

                    if apple: 
                        apples = True
                        ans += 2 + distance

            return (hasApple[u] or apples, ans)
                
        hasApple = {i: apple for (i, apple) in enumerate(hasApple)}

        seen = {0}
        
        graph = defaultdict(lambda: [])
        
        for (u, v) in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        _, ans = helper(0)
        
        return ans 
