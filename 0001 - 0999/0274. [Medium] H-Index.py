# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        citations.sort()
        
        ans = -inf
        
        for (i, val) in enumerate(citations):
            if val != 0: 
                if val >= n - i: 
                    ans = max(ans, n - i)
                    
                else: 
                    ans = max(ans, val)
                    
            else: 
                ans = max(ans, 0)
          
        return ans

class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        def helper(value):
            ans = 0 
            
            for citation in citations: 
                if citation >= value: 
                    ans += 1 
                    
            return ans >= value
                    
        n = len(citations)
        
        start = 0
        end = n + 1
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle):
                start = middle 
            
            else: 
                end = middle 
                
        return start
