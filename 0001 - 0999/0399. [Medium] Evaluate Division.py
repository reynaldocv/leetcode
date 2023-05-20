# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:    
        def helper(num, den):
            stack = [(num, 1)]
            
            seen = set()
            
            while stack: 
                (x, ans) = stack.pop() 
                
                if x == den: 
                    return ans 
                
                for y in graph[x]:
                    if y not in seen: 
                        seen.add(y)
                        
                        stack.append((y, ans*graph[x][y]))
                                     
            return -1 
        
        graph = defaultdict(lambda: {})
        
        for (i, (a, b)) in enumerate(equations):                       
            graph[a][b] = values[i]
            graph[b][a] = 1/values[i]
             
        ans = []
             
        for (num, den) in queries:
            if num not in graph or den not in graph: 
                ans.append(-1)
            
            else: 
                ans.append(helper(num, den))            
            
        return ans 
