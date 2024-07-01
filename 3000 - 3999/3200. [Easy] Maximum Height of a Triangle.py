# https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def helper(first, val, a, b):            
            if first: 
                if val <= a: 
                    return 1 + helper(not first, val + 1, a - val, b)
                
                else: 
                    return 0 
            
            else: 
                if val <= b: 
                    return 1 + helper(not first, val + 1, a, b - val)
                
                else: 
                    return 0 
                
        return max(helper(True, 1, red, blue), helper(False, 1, red, blue))
            
            
