# https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: 
            return 1
        
        ans = lenght = 1
        asc = 1
        
        for i in range(1, n):
            if arr[i - 1] == arr[i]:                
                lenght = 1    
            elif (arr[i - 1] > arr[i] and asc) or (arr[i - 1] < arr[i] and asc == 0):
                asc = 1 - asc    
                lenght += 1
            else:
                lenght = 2
                
            ans = max(ans, lenght)
            
        return ans
                    
                    
            
