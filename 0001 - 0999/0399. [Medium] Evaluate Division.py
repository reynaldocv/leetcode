# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def search(u, end, path, seen):
            for (v, val) in graph[u]:
                if v == end:
                    return path * val
                
                elif v not in seen:
                    seen[v] = True
                    ans = search(v, end, path*val, seen)
                    if ans:
                        return ans
            return None
        
        graph = defaultdict(lambda: [])
        
        for (i, (a, b)) in enumerate(equations):                       
            graph[a].append((b, values[i]))
            graph[b].append((a, values[i]**-1))
             
        ans = []
             
        for (num, den) in queries:
            divisor = search(den, num, 1, {})
            if divisor:
                ans.append(1/divisor)
            else:
                ans.append(-1)
                
        return ans
