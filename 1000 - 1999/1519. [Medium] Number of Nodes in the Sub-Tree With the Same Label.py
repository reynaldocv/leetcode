# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:        
        def helper(u):
            counter = defaultdict(lambda: 0)
            
            for v in graph[u]:
                if v not in seen: 
                    seen.add(v)
                    
                    count = helper(v)
                    
                    for key in count: 
                        counter[key] += count[key]
                    
            idx = index[labels[u]]
            
            counter[idx] += 1 
            
            ans[u] = counter[idx]
            
            return counter
        
        index = {chr(ord("a") + i): i for i in range(26)}
        
        graph = defaultdict(lambda: [])
        
        for (u, v) in edges: 
            graph[u].append(v)
            graph[v].append(u)
            
        seen = {0}
        
        ans = [0 for i in range(n)]
        
        helper(0)
        
        return ans 
