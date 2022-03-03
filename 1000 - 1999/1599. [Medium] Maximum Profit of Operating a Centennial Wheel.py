# https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0 
        onBoard = 0 
        ans = (0, -1)
        n = len(customers)
        rotation = 0 
        i = 0 
        
        while i < n or waiting > 0: 
            waiting += customers[i] if i < n else 0 
            rotation += 1   
            
            if waiting >= 4: 
                onBoard += 4
                waiting -= 4                    
            else: 
                onBoard += waiting
                waiting = 0 

            ans = max(ans, (onBoard*boardingCost - (rotation)*runningCost, -rotation))  
                
            i += 1 
                    
        return -1 if ans[0] <= 0 else -ans[1]
