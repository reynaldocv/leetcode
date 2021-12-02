# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        def helper(idx):
            if len(subsets) <= self.ans: 
                if idx == n: 
                    self.ans = min(self.ans, len(subsets))
                else: 
                    for i in range(len(subsets)):
                        if subsets[i] + tasks[idx] <= sessionTime: 
                            subsets[i] += tasks[idx]
                            helper(idx + 1)
                            subsets[i] -= tasks[idx]
                            
                    subsets.append(tasks[idx])
                    helper(idx + 1)
                    subsets.pop()

        subsets = []
        self.ans = n = len(tasks)
        
        helper(0)
        
        return self.ans
