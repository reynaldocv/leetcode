https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution:
    def maximumLength(self, s: str) -> int:
        counter = defaultdict(lambda: 0)
        
        cnt = 0 
        prev = "$"
        
        for char in s:
            if prev == char: 
                cnt += 1 
                
            else: 
                cnt = 1 
                
            for i in range(1, cnt + 1):
                counter[(char, i)] += 1 
                
            prev = char
                    
        ans = -1
                
        for key in counter: 
            if counter[key] > 2: 
                ans = max(ans, key[1])

        return ans 
                
            
            
        
