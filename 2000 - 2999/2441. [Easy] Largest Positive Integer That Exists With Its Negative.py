# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        
        ans = 0 
        
        for num in nums: 
            if -num in seen: 
                ans = max(ans, abs(num))
                
            seen.add(num)
            
        return -1 if ans == 0 else ans
        
