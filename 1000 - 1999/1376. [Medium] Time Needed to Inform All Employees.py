# https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(lambda: [])
        
        for (i, chief) in enumerate(manager):
            graph[chief].append(i)
            
        stack = [(headID, 0)]        
        ans = 0
        
        while stack: 
            (chief, time) = stack.pop()
            ans = max(ans, time)
            for employee in graph[chief]:
                stack.append((employee, informTime[chief] + time))
            
        return ans
