# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        seen = set()
        
        for (a, b, c) in permutations(digits, 3):
            if a != 0 and c % 2 == 0: 
                num = 100*a + 10*b + c
                
                seen.add(num)
                
        return sorted(seen)
        
            
            
                
                
