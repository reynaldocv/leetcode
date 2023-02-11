# https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(lambda: []))
        
        for (a, b) in redEdges: 
            graph[True][a].append(b)
        
        for (a, b) in blueEdges: 
            graph[False][a].append(b)
            
        stack = [(0, True), (0, False)]        
        seen = {(0, True), (0, False)}
        
        ans = [-1 for _ in range(n)]
        
        steps = 0 
        
        while stack: 
            newStack = []
            
            for (x, blue) in stack: 
                if ans[x] == -1:
                    ans[x] = steps
                
                for y in graph[not blue][x]:
                    if (y, not blue) not in seen:
                        seen.add((y, not blue))
                        
                        newStack.append((y, not blue))
            
            stack = newStack
            steps += 1 
    
        return ans
