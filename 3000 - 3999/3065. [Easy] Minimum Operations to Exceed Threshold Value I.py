# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0 
        
        for num in nums: 
            if num < k: 
                ans += 1 
                
        return ans 
