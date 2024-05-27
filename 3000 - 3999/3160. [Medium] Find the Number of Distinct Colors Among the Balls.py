# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(lambda: 0)
        
        balls = {}
        
        ans = []
        
        for (ith, color) in queries:
            if ith in balls: 
                oldColor = balls[ith]
                
                colors[oldColor] -= 1 
                
                if colors[oldColor] == 0: 
                    colors.pop(oldColor)
                    
            balls[ith] = color
            
            colors[color] += 1 
            
            ans.append(len(colors))
            
        return ans 
                
