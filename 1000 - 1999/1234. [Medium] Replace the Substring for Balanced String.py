# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = {}
        
        for char in s: 
            target[char] = target.get(char, 0) + 1
        
        for key in target:
            target[key] = max(0, target[key] - n//4)
            
        counter = defaultdict(lambda: 0)
        
        ans = n      
        start = 0
        
        for (i, char) in enumerate(s): 
            counter[char] += 1 
            
            while start < n and all(counter[key] >= target[key] for key in target): 
                ans = min(ans, i - start + 1)
                counter[s[start]] -= 1
                start += 1
                
        return ans 
