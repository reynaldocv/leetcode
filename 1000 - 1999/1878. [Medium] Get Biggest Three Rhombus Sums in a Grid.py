# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        sumD1 = [[grid[i][j] for j in range(m)] for i in range(n)]
        sumD2 = [[grid[i][j] for j in range(m)] for i in range(n)]
        
        ans = set([grid[i][j] for i in range(n) for j in range(m)])
        ans = list(ans)
        ans.sort(reverse = True)
        ans = ans[:3]
        
        for i in range(1, n):
            for j in range(1, m):
                sumD1[i][j] += sumD1[i - 1][j - 1]
        
        for i in range(1, n):
            for j in range(m - 1):
                sumD2[i][j] += sumD2[i - 1][j + 1]
        
        for i in range(1, n - 1):
            for j in range(1, m - 1):                
                d = 1
                while 0 <= i - d and i + d < n and 0 <= j - d and j + d < m: 
                    TR = sumD1[i][j + d]
                    TR -= sumD1[i - d - 1][j - 1] if j - 1 >= 0 and i - d - 1 >= 0 else 0 
                    
                    BL = sumD1[i + d][j]
                    BL -= sumD1[i - 1][j - d - 1] if i - 1 >= 0 and j - d - 1 >= 0 else 0
                    
                    TL = sumD2[i - 1][j - d + 1] - sumD2[i - d][j] 
                    
                    BR = sumD2[i + d - 1][j + 1] - sumD2[i][j + d]
                    
                    perimeter = TR + BL + TL + BR
                    
                    if perimeter not in ans: 
                        ans.append(perimeter)
                        ans.sort(reverse = True)
                        ans = ans[:3]
                    d += 1
               
        return ans
                    
