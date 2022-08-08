# https://leetcode.com/problems/task-scheduler-ii/

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        start = defaultdict(lambda: 0)
        
        ans = 0
        
        for task in tasks:
            ans = max(ans + 1, start[task])
            start[task] = ans + space + 1
            
        return ans
                
        
