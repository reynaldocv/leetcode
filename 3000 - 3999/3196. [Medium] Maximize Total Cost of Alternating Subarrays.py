# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        @cache 
        def helper(idx):
            if idx == n: 
                return 0 
            
            else: 
                ans = -inf
                
                tmp = 0 
                sign = 1
                
                for i in range(idx, min(n, idx + 2)):
                    tmp += nums[i]*sign 
                    
                    sign *= -1
                    
                    ans = max(ans, tmp + helper(i + 1))
                    
                return ans 
            
        n = len(nums)
        
        return helper(0)
        
