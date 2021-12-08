# https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isValid(i, j):                        
            nums = defaultdict(lambda: 0)
            for i in range(3):
                for j in range(3):
                    if 1 <= arr[i][j] <= 9:
                        nums[arr[i][j]] += 1
                        if nums[arr[i][j]] > 1: 
                            return False
                    else: 
                        return False
            
            if len(nums) == 9:
                sumS = defaultdict(lambda: 0)
            
                sumS[arr[0][0] + arr[1][1] + arr[2][2]] += 1
                sumS[arr[0][2] + arr[1][1] + arr[2][0]] += 1

                for i in range(3):
                    sumS[arr[i][0] + arr[i][1] + arr[i][2]] += 1
                    sumS[arr[0][i] + arr[1][i] + arr[2][i]] += 1

                if len(sumS) == 1: 
                    return True
                
            else: 
                return False
            
        ans = 0 
        n, m = len(grid), len(grid[0])
        
        for i in range(n - 2):
            for j in range(m - 2):                
                arr = [grid[i][j: j + 3]]
                arr.append(grid[i + 1][j: j + 3])
                arr.append(grid[i + 2][j: j + 3])
                       
                ans += 1 if isValid(i, j) else 0 
                
        return ans
                
            
        
                    
        
