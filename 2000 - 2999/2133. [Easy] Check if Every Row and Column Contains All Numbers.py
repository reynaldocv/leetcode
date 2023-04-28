# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def helper(row):
            seen = set()
            
            for num in row: 
                if num <= n: 
                    seen.add(num)
                    
            return len(seen) == n
        
        n = len(matrix)
        
        for row in matrix: 
            if not helper(row):
                return False 
            
        matrix = [[matrix[i][j] for i in range(n)] for j in range(n)]
        
        for row in matrix: 
            if not helper(row):
                return False
            
        return True
        
        
