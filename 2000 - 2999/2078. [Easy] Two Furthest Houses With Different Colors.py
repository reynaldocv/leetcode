# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0 
        n = len(colors)
        
        for (i, color1) in enumerate(colors):
            for (j, color2) in enumerate(colors):
                if i != j and color1 != color2: 
                    ans = max(ans, abs(i - j))
                    
        return ans
      
class Solution2:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        ans = 0 
        
        for (i, color) in enumerate(colors): 
            if color != colors[0]: 
                ans = max(ans, i)
                
            if color != colors[-1]: 
                ans = max(ans, n - 1 - i)
        
        return ans 
        
        
