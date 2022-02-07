# https://leetcode.com/problems/course-schedule-iv/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @cache
        def helper(x, w):
            for y in graph[x]:
                if y == w or helper(y, w): 
                    return True 
        
            return False 
                    
        graph = defaultdict(lambda: [])
        for (a, b) in prerequisites: 
            graph[b].append(a)
        
        ans = []
        for (a, b) in queries: 
            ans.append(helper(b, a))
            
        return ans
