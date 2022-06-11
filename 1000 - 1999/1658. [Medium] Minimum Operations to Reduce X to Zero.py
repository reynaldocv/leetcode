# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums) 
        
        suffix = defaultdict(lambda: inf)
        
        tmp = 0 
        for (i, num) in enumerate([0] + nums[::-1]):
            tmp += num
            suffix[tmp] = i
            
        prefix = 0 
        
        ans = inf 
        
        for (i, num) in enumerate([0] + nums):
            prefix += num 
            tmp = x - prefix 
            
            if suffix[tmp] + i <= n: 
                ans = min(ans, i + suffix[tmp])
                
        return -1 if ans == inf else ans 
            
            
            
