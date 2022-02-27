# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1 
        
        for char in t: 
            counter[char] -= 1 
            if counter[char] == 0:
                counter.pop(char)
                
        ans = 0 
        for key in counter:
            ans += abs(counter[key])
            
        return ans
        
