# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def counter(word):
            seen = set()
            
            for char in word: 
                if char in seen: 
                    return False 
                
                seen.add(char)
                
            return True
        
        def helper(word, x):
            if x == n:                 
                if counter(word): 
                    return len(word)
                else: 
                    return inf 
            
            else: 
                ans = helper(word, x + 1)
            
                if counter(word + arr[x]):
                    ans = max(ans, helper(word + arr[x], x + 1))
                    
                return ans 
        
        n = len(arr)
        
        return helper("", 0)
        
