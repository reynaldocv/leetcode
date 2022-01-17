# https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def helper(val):
            ans = 0 
            for battery in batteries: 
                ans += min(val, battery)
                
            return ans >= n*val
        
        start = 0 
        end = sum(batteries)//n + 1
        
        while end - start > 1:
            m = (end + start)//2
            if helper(m):
                start = m
            else:
                end = m
                
        return start
        
        
