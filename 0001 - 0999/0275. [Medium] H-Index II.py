# https://leetcode.com/problems/h-index-ii/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        start = 0 
        end = n 
        
        ans = min(citations[0], n)
        
        while end - start > 1: 
            m = (end + start)//2
            if citations[m] > n - m: 
                ans = max(ans, n - m)
                end = m
            else: 
                ans = max(ans, citations[m])
                start = m
            
        return ans
                
            
            
        
