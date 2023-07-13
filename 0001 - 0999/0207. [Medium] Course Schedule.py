# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        @cache
        def helper(u):
            if len(graph[u]) == 0: 
                return True 
            
            else: 
                seen.add(u)
                
                for v in graph[u]:
                    if v in seen or helper(v) == False: 
                        return False 
                    
                seen.remove(u)
                
                return True 
        
        graph = defaultdict(lambda: [])
        
        for (u, v) in prerequisites: 
            graph[v].append(u)

        seen = set() 
        
        for i in range(numCourses):
            if helper(i) == False:
                return False 
            
        return True 
                
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requisites = defaultdict(lambda: 0)
        graph = defaultdict(lambda: [])
                                
        for (u, v) in prerequisites: 
            graph[v].append(u)
            
            requisites[u] += 1 
            
        stack = [i for i in range(numCourses) if requisites[i] == 0]
        seen = {i for i in range(numCourses) if requisites[i] == 0}
        
        while stack: 
            u = stack.pop() 
            
            for v in graph[u]:
                requisites[v] -= 1 
                
                if requisites[v] == 0 and v not in seen: 
                    seen.add(v)
                    
                    stack.append(v)
                    
        return len(seen) == numCourses
                
