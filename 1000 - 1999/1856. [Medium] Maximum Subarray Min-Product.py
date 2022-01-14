# https://leetcode.com/problems/maximum-subarray-min-product/

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        aSum = [0]
        for num in nums: 
            aSum.append(aSum[-1] + num)
        
        ans = 0 
        stack = []
        for (i, num) in enumerate(nums + [-inf]): 
            while stack and stack[-1][1] >= num: 
                _, minElem = stack.pop()
                idx = stack[-1][0] if stack else -1
                
                ans = max(ans, minElem*(aSum[i] - aSum[idx + 1]))
                
            stack.append((i, num))
            
        return ans % MOD
    
            
