# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(lambda: 0)
        high = cnt = 0 
        
        for task in tasks: 
            counter[task] += 1 
            
            if counter[task] > high: 
                high = counter[task]
                
                cnt = 1
            
            elif counter[task] == high: 
                cnt += 1 
                
        return max(len(tasks), (high - 1)*(n + 1) + cnt)
        
