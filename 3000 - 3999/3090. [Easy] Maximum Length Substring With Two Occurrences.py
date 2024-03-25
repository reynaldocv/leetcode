# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/submissions/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = defaultdict(lambda: 0)
        
        index = defaultdict(lambda: defaultdict(lambda: -1))
        
        last = -1
        
        ans = 0 
        
        for (i, char) in enumerate(s):
            counter[char] += 1 
            
            index[char][counter[char]] = i 
            
            last = max(last, index[char][counter[char] - 2])
            
            ans = max(ans, i - last)
            
        return ans 
        
        
        
        
