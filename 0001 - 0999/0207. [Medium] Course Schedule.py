# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        counter = defaultdict(lambda: 0)
        graph = defaultdict(lambda: [])
        
        for [a, b] in prerequisites: 
            graph[a].append(b)
            counter[b] += 1
            
        stack = [course for course in range(numCourses) if counter[course] == 0]
        seen = {course: True for course in range(numCourses) if counter[course] == 0}
        req = defaultdict(lambda: 0)
        
        while stack: 
            v0 = stack.pop(0)
            for v1 in graph[v0]:
                if v1 not in seen: 
                    req[v1] += 1
                    if req[v1] == counter[v1]:
                        seen[v1] = True
                        stack.append(v1)
                        
        return len(seen) == numCourses
                    
                    
                
