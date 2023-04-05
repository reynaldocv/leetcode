# https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0 
        odd = 0 
        
        turn = 1 
        
        while n: 
            bit = n % 2 
            if turn: 
                if bit: 
                    even += 1 
                    
            else: 
                if bit:
                    odd += 1 
                    
            n = n//2
            turn = 1 - turn 
            
        return [even, odd]
            
