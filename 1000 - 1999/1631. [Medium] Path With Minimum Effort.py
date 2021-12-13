# https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights: 
            return 0 
        
        heap = [(0, (0, 0))]
        
        costs = defaultdict(lambda: inf)
        costs[(0, 0)] = 0 
        
        n, m = len(heights), len(heights[0])
        
        ans = 0 
        
        while heap: 
            (cost, (x, y)) = heappop(heap)
            ans = max(ans, cost)
            if (x, y) == (n - 1, m - 1):
                break
            
            for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= r < n and 0 <= s < m: 
                    aux = abs(heights[x][y] - heights[r][s])
                    if aux < costs[(r, s)]:
                        costs[(r, s)] = aux
                        heappush(heap, (aux, (r, s)))
            
        return ans
        
        
      
