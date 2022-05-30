# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt = defaultdict(lambda: 0)
        counter = defaultdict(lambda: 0)
        
        for char in target: 
            counter[char] += 1 
            
        for char in s: 
            if char in counter: 
                cnt[char] += 1 
            
        ans = inf
        for char in target: 
            ans = min(ans, cnt[char]//counter[char])
            
        return ans 
