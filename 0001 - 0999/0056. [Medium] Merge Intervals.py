# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(lambda: 0)
        
        for (a, b) in intervals: 
            counter[a] += 1
            counter[b] -= 1 
            
        coords = [key for key in counter]
        coords.sort()
        
        ans = []
        
        prev = 0 
        
        start = None 
        
        for x in coords: 
            prev += counter[x]
            
            if start == None: 
                start = x 
            
            if prev == 0: 
                ans.append((start, x))
                
                start = None 
                
        return ans 
            
        
        
            
