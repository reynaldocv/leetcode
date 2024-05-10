# https://leetcode.com/problems/simplified-fractions/

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        
        for num in range(1, n + 1):
            for den in range(num + 1, n + 1):
                if gcd(num, den) == 1: 
                    ans.append(str(num) + "/" + str(den))
                    
        return ans 
        
        
