# https://leetcode.com/problems/maximum-subarray-min-product/

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7 
        
        stack = [(-1, -1)]
        
        prefixSum = [0]
        
        ans = 0 
        
        for num in nums: 
            prefixSum.append(prefixSum[-1] + num)
        
        for (i, num) in enumerate(nums + [0]):
            while stack and stack[-1][0] > num: 
                (number, idx) = stack.pop() 
                
                left = stack[-1][1]
                
                ans = max(ans, (prefixSum[i] - prefixSum[left + 1])*number)
                
            stack.append((num, i))
            
        return ans % MOD
            
            
        
            
