# https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(lambda: [])
        for (v0, v1) in edges: 
            graph[v0 - 1].append(v1 - 1)
            graph[v1 - 1].append(v0 - 1)
            
        heap = [(0, 0)]
        seen = [[inf, inf] for _ in range(n)]
        
        least = None
        
        while heap: 
            t, v0 = heappop(heap)
            if v0 == n - 1: 
                if least is None: 
                    least = t
                elif least < t: 
                    return t 
                
            if (t//change) & 1: 
                t = (t//change + 1)*change
            
            t += time
            
            for v1 in graph[v0]: 
                if t != seen[v1][0] and t < seen[v1][1]: 
                    if t < seen[v1][0]: 
                        seen[v1] = [t, seen[v1][0]]
                    else: 
                        seen[v1][1] = t
                        
                    heappush(heap, (t, v1))
