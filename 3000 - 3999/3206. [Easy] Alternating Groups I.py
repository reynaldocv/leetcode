# https://leetcode.com/problems/alternating-groups-i/

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        
        ans = 0 
        
        for i in range(n):
            left = colors[i -  2]
            center = colors[i - 1]
            right = colors[i]
            
            if left != center and center != right: 
                ans += 1 
                
        return ans
        
