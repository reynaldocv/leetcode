# https://leetcode.com/problems/process-tasks-using-servers/

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        busy = []
        free = []
        for (i, server) in enumerate(servers):
            heappush(free, (server, i))
        
        ans = []
        
        for (t, task) in enumerate(tasks):
            while busy and busy[0][0] == t: 
                (_, server, i) = heappop(busy)
                heappush(free, (server, i))
                
            if free: 
                (server, i) = heappop(free)
            else: 
                (t, server, i) = heappop(busy)
                
            ans.append(i)
            heappush(busy, (t + task, server, i))
    
        return ans 
