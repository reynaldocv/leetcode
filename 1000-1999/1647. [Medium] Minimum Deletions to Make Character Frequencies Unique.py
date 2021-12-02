# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = defaultdict(lambda: 0)
        for char in s: 
            counter[char] += 1
            
        seen = {}
        ans = 0
        for char in counter: 
            if counter[char] in seen: 
                while counter[char] in seen: 
                    counter[char] -= 1
                    ans += 1
                     
                if counter[char] != 0: 
                    seen[counter[char]] = True
            else: 
                seen[counter[char]] = True
        
        return ans
        
