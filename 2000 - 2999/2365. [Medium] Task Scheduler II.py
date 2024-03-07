# https://leetcode.com/problems/task-scheduler-ii/

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last = defaultdict(lambda: -1)
        
        ans = 0 
        
        for task in tasks:
            if last[task] < ans: 
                ans += 1 
                
            else: 
                ans = last[task] + 1
                
            last[task] = ans + space 
            
        return ans 
                
                
        
