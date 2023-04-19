# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        
        arr = sorted(heights)
        
        ans = 0 
        
        for i in range(n):
            if arr[i] != heights[i]:
                ans += 1 
                
        return ans 
        
        
