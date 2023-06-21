# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        
        arr = sorted([(nums[i], cost[i]) for i in range(n)])
        
        prefix = [arr[0][1]] + [0 for _ in range(n - 1)]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i][1]
            
        totalCost = 0 
        
        for i in range(1, n):
            totalCost += arr[i][1]*(arr[i][0] - arr[0][0])
            
        ans = totalCost 
        
        for i in range(1, n):
            gap = arr[i][0] - arr[i - 1][0]
            
            totalCost += prefix[i - 1]*gap
            totalCost -= gap*(prefix[n - 1] - prefix[i - 1])
            
            ans = min(ans, totalCost)
            
        return ans 
            
