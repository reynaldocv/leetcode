# https://leetcode.com/problems/cyclically-rotating-a-grid/

class Solution1:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        r1, r2, c1, c2 = 0, n - 1, 0, m - 1
        
        while r1 < r2 and c1 < c2: 
            values = []
            for i in range(c1, c2):
                values.append(grid[r1][i])
                
            for j in range(r1, r2):
                values.append(grid[j][c2])
                
            for i in range(c2, c1, -1):
                values.append(grid[r2][i])                
            
            for j in range(r2, r1, -1):
                values.append(grid[j][c1])
                
            rot = k % (len(values))
            values = values[rot:] + values[:rot]
            
            idx = 0
            for i in range(c1, c2):
                grid[r1][i] = values[idx]
                idx += 1
                
            for j in range(r1, r2):
                grid[j][c2] = values[idx]
                idx += 1
                
            for i in range(c2, c1, -1):
                grid[r2][i] = values[idx]
                idx += 1
            
            for j in range(r2, r1, -1):
                grid[j][c1] = values[idx]
                idx += 1
                
            r1, r2, c1, c2 = r1 + 1, r2 - 1, c1 + 1, c2 - 1
            
        return grid

class Solution2:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        positions = defaultdict(lambda: [])
        values = defaultdict(lambda: [])
        
        total = 0 
        time = 0         
        
        (x, y) = (0, -1)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        l = 0 
        
        seen = {(0, n), (m, n - 1), (m - 1, - 1)}
        
        while total < m*n: 
            x += directions[l][0]
            y += directions[l][1]
            
            if (x, y) in seen: 
                x -= directions[l][0]
                y -= directions[l][1]
                
                l = (l + 1) % 4
                
                if l == 0: 
                    time += 1 
                
            else: 
                total += 1 
                
                seen.add((x, y))
                
                positions[time].append((x, y))
                values[time].append(grid[x][y])

        for key in positions: 
            m = len(positions[key])
            
            for (i, (x, y)) in enumerate(positions[key]):
                grid[x][y] = values[key][(i + k) % m]
                
        return grid
                
                
            
        
