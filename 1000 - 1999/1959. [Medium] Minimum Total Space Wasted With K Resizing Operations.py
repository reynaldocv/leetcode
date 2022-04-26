# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        @cache
        def fn(i, k): 
            if i == n: 
                return 0
            
            if k < 0: 
                return inf 
            
            ans = inf
            rmx = rsm = 0
            for j in range(i, len(nums)): 
                rmx = max(rmx, nums[j])
                rsm += nums[j]
                ans = min(ans, rmx*(j - i + 1) - rsm + fn(j + 1, k - 1))
                
            return ans 
        
        n = len(nums)
        
        return fn(0, k)
