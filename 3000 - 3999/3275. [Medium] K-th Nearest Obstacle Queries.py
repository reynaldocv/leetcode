# https://leetcode.com/problems/k-th-nearest-obstacle-queries/

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        
        ans = []
        
        for (x, y) in queries:
            heappush(heap, -1*(abs(x) + abs(y)))
            
            while len(heap) > k:
                heappop(heap)
                
            if len(heap) < k:
                ans.append(-1)
                
            else:
                ans.append(-1*heap[0])
                
        return ans
