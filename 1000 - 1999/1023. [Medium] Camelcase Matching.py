# https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def helper(query):
            i = 0 
            for char in query: 
                if i < n and char == pattern[i]:
                    i += 1                     
                elif char.isupper():
                    return False 
                
            return i == n
        
        n = len(pattern)
       
        return [helper(query) for query in queries]
            
            
        
