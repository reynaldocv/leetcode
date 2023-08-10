# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        counter = defaultdict(lambda: [])
        
        for (x, y) in rectangles: 
            counter[y].append(x)
            
        for key in counter: 
            counter[key].sort() 
            
        ans = []
        
        for (x, y) in points:             
            tmp = 0 
            
            for num in range(y, 101):
                n = len(counter[num])
            
                tmp += n - bisect_left(counter[num], x)
                
            ans.append(tmp)
                
        return ans 
            
