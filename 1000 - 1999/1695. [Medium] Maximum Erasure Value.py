# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        index = defaultdict(lambda: -1)
        
        start = -1
        ans = 0 
        
        for (i, num) in enumerate(nums): 
            start = max(start, index[num])
            ans = max(ans, prefix[i + 1] - prefix[start + 1])
            
            index[num] = i 
            
        return ans
        
