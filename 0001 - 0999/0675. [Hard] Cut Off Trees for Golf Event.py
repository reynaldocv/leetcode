# https://leetcode.com/problems/cut-off-trees-for-golf-event/

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def helper(start, end):
            ans = 0 
            seen = {start: True}
            stack = [start]
            while stack: 
                newStack = []
                for (x, y) in stack: 
                    if (x, y) == end: 
                        return ans
                    
                    for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0 <= r < n and 0 <= s < m: 
                            if forest[r][s] != 0 and (r, s) not in seen: 
                                seen[(r, s)] = True 
                                newStack.append((r, s))
                    
                stack = newStack    
                ans += 1     
                
            return -1
        
        n, m = len(forest), len(forest[0])
        
        ends = []
        for i in range(n):
            for j in range(m):
                if forest[i][j] > 1: 
                    ends.append((i, j))
                    
        ends.sort(key = lambda item: forest[item[0]][item[1]])
        
        ans = 0 
        start = (0, 0)
        
        for end in ends: 
            val = helper(start, end)
            if val == -1:
                return -1
            
            ans += val
            start = end
            
        return ans
            
