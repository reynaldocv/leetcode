# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mult = 1
        start = -1
        ans = 0
        for (i, num) in enumerate(nums): 
            mult *= num
            if mult > 0: 
                ans = max(ans, i - start)
            elif mult == 0: 
                start = i
                mult = 1
        
        mult = 1
        start = -1
        for (i, num) in enumerate(nums[::-1]): 
            mult *= num
            if mult > 0: 
                ans = max(ans, i - start)
            elif mult == 0: 
                start = i
                mult = 1
        
        return ans
            
        
        
