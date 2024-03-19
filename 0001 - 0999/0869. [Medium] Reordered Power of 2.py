# https://leetcode.com/problems/reordered-power-of-2/

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def helper(number):
            strNum = [char for char in str(number)]
            
            strNum.sort(key = lambda item: item)
            
            return "".join(strNum)
            
        num = 2        
        seen = {"1"}
        
        while num <= 2**32: 
            seen.add(helper(num))
            
            num *= 2 
            
        return helper(n) in seen
            
        
        
