# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        frequency = [0]*(n + 1)
        
        for (start, end) in requests: 
            frequency[start] += 1
            frequency[end + 1] -= 1
            
        for i in range(1, n + 1):
            frequency[i] += frequency[i - 1]
            
        nums.sort()
        frequency.sort()
        
        ans = 0
        for i in range(n):
            ans += nums[i]*frequency[i + 1]
            ans %= MOD
        
        return ans 
            
