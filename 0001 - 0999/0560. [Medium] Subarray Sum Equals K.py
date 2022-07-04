# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(lambda: 0)
        seen[0] += 1 
        
        aSum = 0 
        
        ans = 0 
        
        for num in nums: 
            aSum += num 
            if aSum - k in seen: 
                ans += seen[aSum - k] 
                
            seen[aSum] += 1 
        
        return ans
        
        
        
    
        
