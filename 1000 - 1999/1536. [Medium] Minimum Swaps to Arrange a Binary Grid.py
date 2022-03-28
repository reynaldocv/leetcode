# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0 
        
        zeroesNeeded = n - 1
        start = 1
        
        for i in range(n):
            tmp = i 
            while tmp < n and grid[tmp][start:] != [0 for i in range(zeroesNeeded)]:
                tmp += 1 
                
            if tmp >= n: 
                return -1
            
            start += 1 
            zeroesNeeded -= 1 
            
            while tmp > i: 
                grid[tmp], grid[tmp - 1] = grid[tmp - 1], grid[tmp]
                tmp -= 1 
                ans += 1 
                
        return ans 
