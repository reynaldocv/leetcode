# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(lambda: [])
        
        for (u, v, time) in edges: 
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        heap = [(0, 0)]  
        seen = set()
        
        distance = defaultdict(lambda: inf)
        distance[0] = 0 
        
        while heap: 
            (last, u) = heappop(heap)
            
            if u not in seen:             
                distance[u] = last 
                seen.add(u)

                for (v, units) in graph[u]:
                    if v not in seen: 
                        if last + units < disappear[v]:                    
                            heappush(heap, (last + units, v))
                    
        ans = []
        
        for u in range(n):
            if distance[u] == inf: 
                ans.append(-1)
                
            else: 
                ans.append(distance[u])
                
        return ans
           
