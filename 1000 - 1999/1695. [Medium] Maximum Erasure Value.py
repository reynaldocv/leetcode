# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = [0]
        
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        last = 0
        seen = defaultdict(lambda: 0)
        
        ans = 0 
        
        for (i, num) in enumerate(nums):
            last = max(last, seen[num])
            
            ans = max(ans, prefix[i + 1] - prefix[last])
            
            seen[num] = i + 1 
            
        return ans 
        
        
