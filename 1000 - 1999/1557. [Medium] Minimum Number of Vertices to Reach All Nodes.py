# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        counter = defaultdict(lambda: 0)
        
        for (a, b) in edges: 
            counter[b] += 1 
            
        return [i for i in range(n) if counter[i] == 0]
        
        
