# https://leetcode.com/problems/elimination-game/

class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(start, end, turn, n, ratio):
            if start == end: 
                return start
            
            else: 
                if turn: 
                    start += ratio

                    if n % 2 == 1: 
                        end -= ratio
                        
                else: 
                    if n % 2 == 1: 
                        start += ratio
                    
                    end -= ratio
                    
                return helper(start, end, not turn, n//2, 2*ratio)
                
        return helper(1, n, True, n, 1)
        
            
        
