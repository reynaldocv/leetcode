# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def helper(word):
            ans = ""
            seen = {}
            i = 0
            for char in word: 
                if char not in seen: 
                    ans += chr(i + ord("a"))
                    seen[char] = chr(i + ord("a"))
                    i += 1
                else: 
                    ans += seen[char]
                    
            return ans
                    
        pattern = helper(pattern)
        
        ans = []
        for word in words: 
            if pattern == helper(word):
                ans.append(word)
                
        return ans
                
        
                
        
