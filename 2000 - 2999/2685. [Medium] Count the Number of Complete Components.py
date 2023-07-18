# https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def helper(son):
            while parents[son] != son:
                son = parents[son]
                
            return son 
        
        parents = [i for i in range(n)]
        
        degree = defaultdict(lambda: 0)
        
        for (u, v) in edges: 
            parentU = helper(u)
            parentV = helper(v)
            
            degree[u] += 1 
            degree[v] += 1
            
            parents[parentU] = parents[parentV] = min(parentU, parentV)
            
        counter = defaultdict(lambda: [0, 0])
        
        for i in range(n):
            u = helper(i)
            
            counter[u][0] += degree[i]
            counter[u][1] += 1 
            
        ans = 0 
        
        for key in counter:
            cnt = counter[key][1]
            
            if cnt*(cnt - 1) == counter[key][0]:
                ans += 1
            
        return ans    
