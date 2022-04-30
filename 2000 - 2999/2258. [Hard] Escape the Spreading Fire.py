# https://leetcode.com/problems/escape-the-spreading-fire/

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int: 
        def helper(value):
            stack = [(0, 0)]
            seen = {(0, 0)}
            
            time = value + 1
            while stack: 
                newStack = []
                for (x, y) in stack: 
                    for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0 <= r < m and 0 <= s < n: 
                            if grid[r][s] == 0 and (r, s) not in seen: 
                                if r == m - 1 and s == n - 1: 
                                    if time <= flames[-1][-1]:
                                        return True 
                                if time < flames[r][s]:
                                    seen.add((r, s))
                                    newStack.append((r, s))

                stack = newStack
                time += 1
                
            return False 
            
        m, n = len(grid), len(grid[0])
       
        flames = [[inf for j in range(n)] for i in range(m)]
        
        stack = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        for (i, j) in stack: 
            flames[i][j] = 0 
        
        seen = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        
        time = 1
        while stack: 
            newStack = []
            for (x, y) in stack: 
                for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < m and 0 <= s < n: 
                        if grid[r][s] == 0 and (r, s) not in seen: 
                            flames[r][s] = time 
                            seen.add((r, s))
                            newStack.append((r, s))
                            
            time += 1 
            stack = newStack
            
        start = -1 
        end = 10**9 + 1
        
        while end - start > 1: 
            mid = (end + start)//2
            if helper(mid):
                start = mid 
            else: 
                end = mid 
                
        return start
