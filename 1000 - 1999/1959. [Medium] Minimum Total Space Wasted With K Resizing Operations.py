# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        @cache
        def helper(i, k): 
            if i == n: 
                return 0 
            
            if k < 0: 
                return inf 
            
            ans = inf 
            aSum = maxElem = 0 
            
            for j in range(i, n):
                maxElem = max(maxElem, nums[j])
                aSum += nums[j]
                
                ans = min(ans, (j - i + 1)*maxElem - aSum + helper(j + 1, k - 1))
                
            return ans 
            
        n = len(nums)
        
        return helper(0, k)
