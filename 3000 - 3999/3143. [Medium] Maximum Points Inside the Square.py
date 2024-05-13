# https://leetcode.com/problems/maximum-points-inside-the-square/submissions/

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        n = len(s)
        
        chars = defaultdict(lambda: [])
        
        for (i, (x, y)) in enumerate(points):
            key = max(abs(x), abs(y))
            
            chars[key].append(s[i])
            
        arr = [key for key in chars]        
        arr.sort()  
        
        ans = 0 
        
        seen = set()
        
        for num in arr: 
            ans = len(seen)
            
            for char in chars[num]:
                if char in seen: 
                    return ans 
                
                else: 
                    seen.add(char)
                    
        return len(seen)
