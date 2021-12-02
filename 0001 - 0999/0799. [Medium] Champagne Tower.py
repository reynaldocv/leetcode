# https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0: 
            return 0 
        
        arr = [0]*(query_row + 1)
        arr[0] = poured
        
        for i in range(1, query_row + 1):
            arr2 = [0]*(query_row + 1)
            for j in range(i + 1):
                if j == 0:
                    arr2[j] += (arr[j] - 1)/2 if (arr[j] > 1) else 0
                elif j == i:
                    arr2[j] += (arr[j - 1] - 1)/2 if (arr[j - 1] > 1) else 0
                else: 
                    arr2[j] += (arr[j] - 1)/2 if (arr[j] > 1) else 0
                    arr2[j] += (arr[j - 1] - 1)/2 if (arr[j - 1] > 1) else 0
            arr = arr2         
        
        return 1 if (arr[query_glass] >= 1) else arr[query_glass]
                    
        
        
