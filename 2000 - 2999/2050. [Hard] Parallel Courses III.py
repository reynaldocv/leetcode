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

class Solution2:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:        
        times = defaultdict(lambda: 0)
        requisites = defaultdict(lambda: 0)
        graph = defaultdict(lambda: [])
        
        time.insert(0, 0)
        
        for (u, v) in relations: 
            graph[u].append(v)
            
            requisites[v] += 1 
            
        stack = [i for i in range(1, n + 1) if requisites[i] == 0]
        
        for u in stack: 
            times[u] = time[u]            
        
        while stack: 
            u = stack.pop()
            
            for v in graph[u]:
                requisites[v] -= 1 
                
                if requisites[v] == 0: 
                    stack.append(v)
                    
                times[v] = max(times[v], times[u] + time[v])
                
        return max(times[i] for i in range(1, n + 1))
                    
                    
            
            
