# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist) 
        
        arr = []
        
        for i in range(n):
            arr.append(dist[i]/speed[i])
            
        arr.sort() 
        
        last = 0 
        ans = 0 
        
        for (i, num) in enumerate(arr):
            if num > i: 
                ans += 1 
                
            else: 
                break 
                
        return ans 
