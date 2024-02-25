# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        
        sequence = []
        
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                sequence.append(1)
            
            elif nums[i] == nums[i + 1]:
                sequence.append(0)
                
            else: 
                sequence.append(- 1)
                
        ans = 0 
                
        for i in range(n - m):
            if sequence[i: i + m] == pattern: 
                ans += 1 
                
        return ans 
        
