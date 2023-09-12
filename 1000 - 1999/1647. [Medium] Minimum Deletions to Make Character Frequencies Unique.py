# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1
            
        seen = set()        
        ans = 0
        
        for key in counter: 
            if counter[key] in seen: 
                while counter[key] in seen: 
                    counter[key] -= 1
                    
                    ans += 1
                     
                if counter[key] != 0: 
                    seen.add(counter[key])
                    
            else: 
                seen.add(counter[key])
        
        return ans
        
