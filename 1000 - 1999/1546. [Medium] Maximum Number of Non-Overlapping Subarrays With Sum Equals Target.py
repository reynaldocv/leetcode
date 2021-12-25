# https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prev = 0 
        seen = {0: -1}
        last = -inf
        ans = 0 
        
        for (i, num) in enumerate(nums):
            prev += num
            numB = prev - target
            if numB in seen: 
                if last <= seen[numB]:
                    ans += 1
                    last = i 
                    
            seen[prev] = i
            
        return ans
                
        
        
        
        
