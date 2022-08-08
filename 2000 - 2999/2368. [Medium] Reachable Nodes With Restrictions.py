# https://leetcode.com/problems/reachable-nodes-with-restrictions/

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(lambda: [])
        
        for (a, b) in edges: 
            graph[a].append(b)
            graph[b].append(a)
            
        seen = {0}    
        stack = [0]
        
        restricted = {node for node in restricted}
        
        while stack: 
            u = stack.pop() 
            
            for v in graph[u]:
                if v not in restricted and v not in seen: 
                    stack.append(v)
                    seen.add(v)
                    
        return len(seen)
    
