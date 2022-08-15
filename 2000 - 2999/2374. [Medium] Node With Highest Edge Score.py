# https://leetcode.com/problems/node-with-highest-edge-score/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans = (inf, inf)
        counter = defaultdict(lambda: 0)
        
        for (i, v) in enumerate(edges):
            counter[v] -= i
            
            ans = min(ans, (counter[v], v))
            
        return ans[1]
                                       
