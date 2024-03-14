# https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = defaultdict(lambda: 0)
        
        counter[0] = 1 
        
        ans = prev = 0 
        
        for num in nums: 
            prev += num
            
            ans += counter[prev - goal]
            
            counter[prev] += 1 
            
        return ans 
            
            
            
