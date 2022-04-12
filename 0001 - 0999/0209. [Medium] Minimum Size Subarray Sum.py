# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        left = 0 
        aSum = 0 
        for i in range(n):
            aSum += nums[i]
            while aSum >= target: 
                ans = min(ans, i - left + 1)
                aSum -= nums[left]
                left += 1
                
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
            
        
                
            
            
        
