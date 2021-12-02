# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: [])
        counter = defaultdict(lambda: 0)
        
        for (a, b) in prerequisites: 
            graph[b].append(a)
            counter[a] += 1
            
        req = defaultdict(lambda: 0)
        ans = [u for u in range(numCourses) if counter[u] == 0]
        stack = [u for u in range(numCourses) if counter[u] == 0]
        seen = {u: True for u in range(numCourses) if counter[u] == 0}
        
        while stack: 
            u = stack.pop(0)
            for v in graph[u]:
                if v not in seen: 
                    req[v] += 1
                    if req[v] == counter[v]:
                        seen[v] = True
                        stack.append(v)
                        ans.append(v)
                        
        return ans if numCourses == len(seen) else []
        
            
        
