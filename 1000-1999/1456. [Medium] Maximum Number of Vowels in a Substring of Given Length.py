# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k == 1: 
            return 1
        else: 
            n = len(s)
            count = 0
            for i in range(k):
                if s[i] in "aeiou":
                    count += 1            
            ans = count       
            
            for i in range(k, n):
                print(i, s[i], s[i - k], ans)
                if s[i] in "aeiou":
                    count += 1
                if s[i - k] in "aeiou":
                    count -= 1
                ans = max(ans, count)
             
            return ans
                    
                
                
