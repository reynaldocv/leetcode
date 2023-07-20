# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: [])
        cntReq = defaultdict(lambda: 0)
        
        for (a, b) in prerequisites: 
            graph[b].append(a)
            
            cntReq[a] += 1 
            
        ans = [i for i in range(numCourses) if cntReq[i] == 0]
        stack = [i for i in range(numCourses) if cntReq[i] == 0]
        
        seen = {i for i in range(numCourses) if cntReq[i] == 0}
        
        while stack: 
            u = stack.pop(0)
            
            for v in graph[u]:
                cntReq[v] -= 1 
                
                if cntReq[v] == 0 and v not in seen:
                    seen.add(v)
                    
                    ans.append(v)                    
                    stack.append(v)
                    
        m = len(ans)
        
        if m == numCourses: 
            return ans 
        
        else: 
            return []
        
            
        
