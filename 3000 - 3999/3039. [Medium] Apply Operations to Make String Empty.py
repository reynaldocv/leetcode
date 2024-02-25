# https://leetcode.com/problems/apply-operations-to-make-string-empty/

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counter = defaultdict(lambda: 0)        
        maxCnt = 0 
        
        for char in s: 
            counter[char] += 1 
            
            maxCnt = max(maxCnt, counter[char])
        
        ans = ""
        
        counter = defaultdict(lambda: 0)        
        
        for char in s:
            counter[char] += 1 
            
            if counter[char] == maxCnt:
                ans += char 
                
        return ans 
