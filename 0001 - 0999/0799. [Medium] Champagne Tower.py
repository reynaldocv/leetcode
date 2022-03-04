# https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0: 
            return 0 
        
        arr = [poured]
        
        for i in range(1, query_row + 1):
            arr2 = [0 for _ in range(i + 1)]
            for j in range(i):
                liquid = (arr[j] - 1)/2
                if liquid > 0:
                    arr2[j] += liquid
                    arr2[j + 1] += liquid
                
            arr = arr2
            
        return 1 if arr[query_glass] > 1 else arr[query_glass]
                
                    
                
        
        
