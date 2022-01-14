# https://leetcode.com/problems/numbers-with-repeated-digits/

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        @cache 
        def helper(a, b):
            if b == 0: 
                return 1
            
            return a*helper(a - 1, b - 1)
        
        digits = [int(char) for char in str(n)]
        l = len(digits)
        
        if l < 2:
            return 0 
        
        ans = 0 
        for k in range(l - 1):
            ans += 9*helper(9, k)
            
        ans += (digits[0] - 1)*helper(9, l - 1)
        selected = {digits[0]}
        
        idx = 1
        for d in digits[1:]:
            idx += 1
            nchoice = d - sum(x < d for x in selected)
            ans += nchoice * helper(10 - idx, l - idx)
            if d in selected:
                break
            selected.add(d)
        else:
            ans += 1
        return n - ans
