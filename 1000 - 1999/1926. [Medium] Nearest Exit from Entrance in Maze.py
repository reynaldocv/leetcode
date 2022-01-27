# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        
        stack = [entrance]
        seen = {(entrance[0], entrance[1]): True}
        
        ans = 0 
        while stack: 
            ans += 1 
            newStack = []
            for (x, y) in stack: 
                for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < n and 0 <= s < m: 
                        if maze[r][s] == "." and (r, s) not in seen: 
                            seen[(r, s)] = True
                            newStack.append((r, s))
                            if r in [0, n - 1] or s in [0, m - 1]:
                                return ans            
            stack = newStack
            
        return -1
                        
