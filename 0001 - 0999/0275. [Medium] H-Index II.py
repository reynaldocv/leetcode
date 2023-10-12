# https://leetcode.com/problems/h-index-ii/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        start = 0
        end = citations[-1] + 1
        
        while end - start > 1: 
            middle = (end + start)//2
            
            idx = bisect_left(citations, middle)
            
            qnt = n - idx
            
            if middle <= qnt: 
                start = middle
                
            else: 
                end = middle 
                
        return start
                
            
            
        
