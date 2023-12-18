# https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        counter = {i: 1 for i in range(1, n*n + 1)}      
           
        ans = [0, 0]
        
        for row in grid: 
            for num in row: 
                counter[num] += 1 
                
        ans[0] = [key for key in counter if counter[key] == 3][0]
        ans[1] = [key for key in counter if counter[key] == 1][0]
        
        return ans 
