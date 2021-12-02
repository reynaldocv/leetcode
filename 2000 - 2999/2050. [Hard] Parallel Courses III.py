# https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        inDeg = [0 for _ in range(n)]
        
        for (u, v) in relations: 
            graph[u - 1].append(v - 1)
            inDeg[v - 1] += 1
        
        heap = []
        
        for (i, x) in enumerate(inDeg):
            if x == 0: 
                heappush(heap, (time[i], i))
                
        while heap: 
            (t, u) = heappop(heap)
            for v in graph[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0: 
                    heappush(heap, (t + time[v], v))
        
        return t
            
            
