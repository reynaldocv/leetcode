# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        last = 0 
        
        ans = (0, -1)
        
        for (idx, time) in logs: 
            ans = max(ans, (time - last, -idx))
            
            last = time            
            
        return -ans[1]
        
