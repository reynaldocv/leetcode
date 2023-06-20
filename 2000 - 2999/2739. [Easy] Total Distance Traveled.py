# https://leetcode.com/problems/total-distance-traveled/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        def helper(n, m):
            if n < 5: 
                return 10*n 
            
            elif n >= 5: 
                if m > 0: 
                    return 50 + helper(n - 5 + 1, m - 1)
                
                else: 
                    return 50 + helper(n - 5, 0)
                
        return helper(mainTank, additionalTank)
