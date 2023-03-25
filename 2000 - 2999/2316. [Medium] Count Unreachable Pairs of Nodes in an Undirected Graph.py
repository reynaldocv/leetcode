# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def helper(son):
            while parent[son] != son: 
                son = parent[son]
                
            return son 
        
        parent = [i for i in range(n)]
        
        for (a, b) in edges: 
            parentA = helper(a)
            parentB = helper(b)
            
            parent[parentA] = parent[parentB] = min(parentA, parentB)
            
        ans = n*(n + 1)//2
        
        counter = defaultdict(lambda: 0)
        
        for i in range(n):
            parentI = helper(i)            
            counter[parentI] += 1 
            
            ans -= counter[parentI]
            
        return ans 
            
            
