# https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = n + len(rolls)
        aSum = total*mean - sum(rolls)
        
        quo = aSum // n
        
        res = aSum % n
        
        ans = []
        if aSum % n == 0: 
            if 1 <= quo <= 6: 
                ans = [quo]*n
        else: 
            if 1 <= quo <= 5: 
                ans = [quo + 1]*res + [quo]*(n - res)
        
        return ans            
