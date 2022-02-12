# https://leetcode.com/problems/closest-divisors/

class Solution:
    def closestDivisors(self, num: int) -> List[int]:        
        num1, num2 = num + 1, num + 2
        
        sqrt1 = int((num1)**0.5) + 1
        sqrt2 = int((num2)**0.5) + 1
        
        while sqrt1 >= 2 or sqrt2 >= 2:
            if (num2) % sqrt2 == 0:
                return [sqrt2, num2//sqrt2]
            
            if (num1) % sqrt1 == 0:
                return [sqrt1, num1//sqrt1]
            
            sqrt1 -= 1
            sqrt2 -= 1

        return [1, sqrt1]
