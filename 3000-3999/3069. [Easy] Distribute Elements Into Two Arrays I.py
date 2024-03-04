# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0 
        
        for num in nums: 
            if num < k: 
                ans += 1 
                
        return ans 
