# https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(lambda: []))
        for (a, b) in redEdges: 
            graph[a][True].append(b)
        
        for (a, b) in blueEdges: 
            graph[a][False].append(b)
            
        stack = [(-1, 0, True, True), (-1, 0, False, False)]        
        
        ans = [-1 for _ in range(n)]
        steps = 0 
        dictSeen = {True: {}, False: {}} 
        
        while stack: 
            newStack = []
            for (_, x, blue, seen) in stack: 
                if ans[x] == -1:
                    ans[x] = steps
                
                for y in graph[x][not blue]:
                    if (x, y, not blue) not in dictSeen[seen]:
                        dictSeen[seen][(x, y, not blue)] = True
                        newStack.append((x, y, not blue, seen))
            
            stack = newStack
            steps += 1 
    
        return ans
