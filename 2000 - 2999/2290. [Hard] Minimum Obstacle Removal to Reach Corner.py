# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        heap = [(0, 0, 0)]
        distance = defaultdict(lambda: inf)
        distance[(0, 0, 0)] = 0 
        
        while heap: 
            (time, x, y) = heappop(heap)
            if x == m - 1 and y == n - 1: 
                return time
            
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s 
                
                if 0 <= p < m and 0 <= q < n: 
                    if time + grid[p][q] < distance[(p, q)]: 
                        distance[(p, q)] = time + grid[p][q]
                        heappush(heap, (time + grid[p][q], p, q))
        
        return distance[(m - 1, n - 1)]
                

class Solution2:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def helper(x, y):
            ans = [(x, y)]
            
            stack = [(x, y)]
            
            while stack: 
                (x, y) = stack.pop(0)
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    if 0 <= p < m and 0 <= q < n: 
                        if grid[p][q] == 0 and (p, q) not in seen:
                            stack.append((p, q))                            
                            ans.append((p, q))
                            seen.add((p, q))
                       
            return ans
        
        m, n = len(grid), len(grid[0])
                
        seen = {(0, 0)}            
        stack = [(0, 0)]
        
        ans = 0 
        
        while stack: 
            newStack = []
            for (x, y) in stack: 
                if x == m - 1 and y == n - 1: 
                    return ans - 1
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    if 0 <= p < m and 0 <= q < n: 
                        if grid[p][q] == 0 and (p, q) not in seen: 
                            seen.add((p, q))                            
                            newStack += helper(p, q)                            
                            
            stack = stack + newStack
            newStack = []
            
            for (x, y) in stack: 
                if x == m - 1 and y == n - 1: 
                    return ans
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    if 0 <= p < m and 0 <= q < n: 
                        if (p, q) not in seen:                             
                            newStack.append((p, q))
                            seen.add((p, q))
            stack = newStack
            ans += 1 
        
            
            
