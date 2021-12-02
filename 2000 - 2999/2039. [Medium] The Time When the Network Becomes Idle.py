# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        
        def helper():
            distances = [inf]*n  
            distances[0] = 0
            seen = {0: True}
            stack = [0]
            while stack: 
                v0 = stack.pop(0)
                for v1 in destiny[v0]:
                    if v1 not in seen: 
                        seen[v1] = True
                        distances[v1] = min(distances[v1], 2 + distances[v0])
                        stack.append(v1)
            
            return distances
            
        n = len(patience)
        destiny = defaultdict(lambda:[])
        for (v0, v1) in edges: 
            destiny[v0].append(v1)
            destiny[v1].append(v0)
        
        distances = helper()
        
        ans = 0
        
        for i in range(1, n):
            last = 0 
            if (distances[i]) % patience[i] == 0: 
                last = (distances[i]) - patience[i]
            else: 
                last = (distances[i]) - ((distances[i]) % patience[i])
                
            ans = max(ans, last + distances[i])
            
        return ans + 1 
            
            
        
        
