# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(lambda: 0)
        seen[0] += 1 
        
        ans = prev = 0 
        
        for num in nums: 
            prev += num 
            
            ans += seen[prev - k]
            
            seen[prev] += 1 
            
        return ans 
            
            
        
        
    
        
