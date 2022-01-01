# https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        seen = {}
        time = 0
        n = len(grid)
        
        while heap: 
            (cur, x, y) = heappop(heap)
            seen[(x, y)] = True
            time = max(time, cur)
            if x == n - 1 and y == n - 1: 
                return time
            
            for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= r < n and 0 <= s < n:
                    if (r, s) not in seen: 
                        seen[(r, s)] = True
                        heappush(heap, (grid[r][s], r, s))
                        
        return -1
