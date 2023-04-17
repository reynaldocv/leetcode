# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        def helper(word, character):
            ans = [0]
            
            counter = 0 
            
            for char in word: 
                if char == character:
                    counter += 1 
                    
                ans.append(counter)
                
            return ans 
        
        n = len(s)
        
        left = helper(s, "a")
        right = helper(s[:: -1], "b")[:: -1]
        
        ans = inf 
        
        for i in range(n + 1):
            ans = min(ans, n - left[i] - right[i])
            
        return ans 
