# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def helper(son):
            while son != parent[son]:
                son = parent[son]
                
            return son 
        
        def collaborator(son1, son2):
            parent1 = helper(son1)
            parent2 = helper(son2)
            
            parent[parent1] = parent[parent2] = min(parent1, parent2)
            
        parent = [i for i in range(n)]
        
        for (a, b)  in edges: 
            collaborator(a, b)
            
        counter = defaultdict(lambda: 0)
        
        for i in range(n):
            counter[helper(i)] += 1 
        
        ans = n*(n - 1)
        
        for key in counter: 
            ans -= (counter[key] - 1)*counter[key]
            
        return ans//2
            
            
