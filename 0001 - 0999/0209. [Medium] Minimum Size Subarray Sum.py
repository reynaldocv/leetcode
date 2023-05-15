# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        ans = inf
        
        prev = 0 
        start = 0
        
        for (i, num) in enumerate(nums):
            prev += num 
                
            while start <= i and prev >= target: 
                ans = min(ans, i - start + 1)
                
                prev -= nums[start]
                start += 1 
                
        return ans if ans != inf else 0 
        
class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        for num in nums: 
            prefix.append(prefix[-1] + num)
            
        m = len(prefix)
        
        ans = inf
        
        for (i, num) in enumerate(prefix): 
            val = num + target
            idx = bisect_left(prefix, val)
            
            if idx < m: 
                ans = min(ans, idx - i)
                
        return 0 if ans == inf else ans 
            
        
                
            
            
        
