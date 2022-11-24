# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = defaultdict(lambda :0)
        
        ans = (0, -1)
        
        for (a, b) in edges: 
            counter[a] += 1 
            counter[b] += 1 
            
            ans = max(ans, (counter[a], a), (counter[b], b))
            
        return ans[1]
            
