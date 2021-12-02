# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        counter = 0
        for i in range(len(s)):
            counter = counter + 1 if (s[i] == "L") else counter - 1
            ans = ans + 1 if (counter == 0) else ans
        return ans
        
        
