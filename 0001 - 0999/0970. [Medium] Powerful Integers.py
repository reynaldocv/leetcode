# https://leetcode.com/problems/powerful-integers/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        first = [1]
        second = [1]
        
        if x > 1: 
            while first[-1] < bound: 
                first.append(first[-1]*x) 
        if y > 1: 
            while second[-1] < bound: 
                second.append(second[-1]*y) 

        seen = set()
        
        for num1 in first: 
            for num2 in second: 
                if (num1 + num2 <= bound):
                    seen.add(num1 + num2)
                    
                else: 
                    break 
                    
        return seen
