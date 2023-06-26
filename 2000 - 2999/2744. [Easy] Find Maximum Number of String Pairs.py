# https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        
        ans = 0 
        
        for word in words: 
            if word[:: -1] in seen: 
                ans += 1 
                
            seen.add(word)
            
        return ans 
        
