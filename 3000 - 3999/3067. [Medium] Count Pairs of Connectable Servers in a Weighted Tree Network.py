# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        @cache 
        def helper(u, parent, path):
            ans = 0 
            
            if path == 0:
                ans = 1 
                
            for (v, distV) in graph[u]:
                if v != parent: 
                    ans += helper(v, u, (path + distV) % signalSpeed)
                
            return ans 
        
        n = len(edges) + 1
        
        graph = defaultdict(lambda: [])
        
        for (u, v, dist) in edges:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            
        ans = [0 for _ in range(n)]
        
        for root in range(n):
            branches = graph[root]
            
            m = len(branches)
            
            for i in range(m):
                for j in range(i + 1, m):
                    (u, distU) = branches[i]
                    (v, distV) = branches[j]
                    
                    ans[root] += helper(u, root, distU % signalSpeed)*helper(v, root, distV % signalSpeed)
                    
        return ans 
