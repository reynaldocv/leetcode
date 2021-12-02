# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        aux = ""
        n = len(s)
        counter = 0
        ans = ""
        for i in range(n):
            if s[i] == aux: 
                counter += 1
                if counter <= 2: 
                    ans += s[i]
                    
            else: 
                aux = s[i]
                counter = 1
                ans += s[i]
        return ans
                    
