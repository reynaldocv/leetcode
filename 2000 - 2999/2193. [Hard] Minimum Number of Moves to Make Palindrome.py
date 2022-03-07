# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        n = len(s)
        ans = 0
        
        for left in range(n//2):
            right = n - left - 1
            
            if s[left] != s[right]:
                start = left
                end = right
                
                while s[left] != s[end]:
                    end -= 1
                    
                while s[right] != s[start]:
                    start += 1
                    
                if right - end < start - left:
                    ans += right - end
                    for i in range(end, right):
                        s[i] = s[i + 1]
                else:
                    ans += start - left
                    for i in range(start, left, -1):
                        s[i] = s[i - 1]
                        
        return ans
