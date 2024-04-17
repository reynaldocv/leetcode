# https://leetcode.com/problems/flower-planting-with-no-adjacent/

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: [])
        
        for (u, v) in paths: 
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
            
        heap = []
        
        for i in range(n):
            heappush(heap, (-len(graph[i]), i))
        
        ans = [0 for _ in range(n)]
        
        while heap:
            (_, u) = heappop(heap)
            
            colours = set()
            
            for v in graph[u]:
                colours.add(ans[v])
                
            for colour in range(1, 5):
                if colour not in colours: 
                    break 
                    
            ans[u] = colour
            
        return ans 
            
            
        
        
