# https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort() 
        
        extra = sum(batteries[: -n])
        
        live = batteries[-n: ]
                
        for i in range(n - 1):
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra//(i + 1)
            
            extra -= (i + 1) * (live[i + 1] - live[i])
            
        return live[-1] + extra // n
            
class Solution2:
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
        
        
