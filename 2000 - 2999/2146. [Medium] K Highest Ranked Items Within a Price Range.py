# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        x, y = start[0], start[1]
        seen = {(x, y): True}
        
        n, m = len(grid), len(grid[0])
        stack = [(x, y)]
        
        ans = []
        if pricing[0] <= grid[x][y] <= pricing[1]:                                
            ans.append((0, grid[x][y], x, y))
        
        dist = 1
        while stack: 
            newStack = []
            for (x, y) in stack:                 
                for (r, s) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if 0 <= r < n and 0 <= s < m: 
                        if grid[r][s] != 0 and (r, s) not in seen: 
                            seen[(r, s)] = True
                            if pricing[0] <= grid[r][s] <= pricing[1]:                                
                                ans.append((dist, grid[r][s], r, s))
                            newStack.append((r, s))
            
            stack = newStack
            dist += 1 
            
                        
        ans.sort()
        
        return [(x, y) for (_, _, x, y) in ans[:k]]
                        
                        
