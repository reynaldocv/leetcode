# https://leetcode.com/problems/node-with-highest-edge-score/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans = (0, 0)
        
        counter = defaultdict(lambda: 0)
        
        for (u, v) in enumerate(edges): 
            counter[v] += u 
            
            ans = max(ans, (counter[v], -v))
            
        return -ans[1]
        
                                       
