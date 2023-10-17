# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution:
    def numSplits(self, s: str) -> int:
        right = defaultdict(lambda: 0)
        
        for char in s: 
            right[char] += 1 
            
        left = defaultdict(lambda: 0) 
            
        ans = 0 
            
        for char in s: 
            left[char] += 1             
            right[char] -= 1 
            
            if right[char] == 0: 
                right.pop(char)
                
            if len(left) == len(right):
                ans += 1 
                
        return ans 
            
            
