# https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache 
        def helper(x):
            if manager[x] == -1: 
                return informTime[x]
            
            else: 
                return informTime[x] + helper(manager[x])
        
        return max(helper(i) for i in range(n))

class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(lambda: [])
        
        for (i, chief) in enumerate(manager):
            graph[chief].append(i)
            
        stack = [(headID, 0)]
        
        ans = 0 
        
        while stack: 
            (x, time) = stack.pop(0) 
            
            ans = max(ans, time)
            
            for y in graph[x]:
                stack.append((y, time + informTime[x]))
                
        return ans 

