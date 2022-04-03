# https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x, y = target 
        
        for (r, s) in ghosts: 
            if abs(r - x) + abs(s - y) <= abs(x) + abs(y):
                return False
            
        return True 
