# https://leetcode.com/problems/describe-the-painting/

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(lambda: 0)

        for (u, v, paint) in segments: 
            counter[u] += paint
            counter[v] -= paint
            
        coord = [key for key in counter]
        
        coord.sort() 
        
        ans = []
        
        prev = 0        
        start = 0 
        
        for x in coord: 
            if prev != 0: 
                ans.append((start, x, prev))
                
            prev += counter[x]
            start = x 
            
        return ans 
        
