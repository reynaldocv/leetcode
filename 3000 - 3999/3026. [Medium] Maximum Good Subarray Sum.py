# https://leetcode.com/problems/maximum-good-subarray-sum/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        aSum = 0 
        
        ans = -inf
        
        index = defaultdict(lambda: inf)
        
        for (i, num) in enumerate(nums):
            aSum += num 
            
            greater = num + k            
            if greater in index: 
                ans = max(ans, aSum - index[greater])            
            
            lower = num - k             
            if lower in index: 
                ans = max(ans, aSum - index[lower])            
           
            index[num] = min(index[num], aSum - num)
            
        return 0 if ans == -inf else ans 
        
        
        
