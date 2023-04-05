# https://leetcode.com/problems/minimize-maximum-of-array/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        aSum = 0 
        
        ans = 0 
        
        for (i, num) in enumerate(nums):
            aSum += num 
            
            tmp = aSum // (i + 1)
            
            if aSum % (i + 1) != 0: 
                tmp += 1 
            
            ans = max(ans, tmp)
        
        return ans 

