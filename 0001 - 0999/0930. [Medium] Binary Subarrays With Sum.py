# https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(lambda: 0)
        seen[0] = 1
        
        ans = 0 
        prev = 0 
        
        for num in nums:             
            prev += num
            diff = prev - goal
            if diff in seen:
                ans += seen[diff]
            
            seen[prev] += 1
            
        return ans
            
            
            
