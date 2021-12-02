# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        n = len(nums)        
        counter = defaultdict(lambda: 0)
        ans = 0 
        aSum = 0 
        for i in range(n):
            aSum += nums[i]
            if aSum == k: 
                ans += 1
            if aSum - k in counter: 
                ans += counter[aSum - k]
            counter[aSum] += 1
        
        return ans
        
        
        
        
    
        
