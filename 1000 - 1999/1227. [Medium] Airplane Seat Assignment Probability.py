# https://leetcode.com/problems/airplane-seat-assignment-probability/

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        def helper(n):
            if n >= 2: 
                return 0.5
            else: 
                return 1.0 
            
        return helper(n)
        
