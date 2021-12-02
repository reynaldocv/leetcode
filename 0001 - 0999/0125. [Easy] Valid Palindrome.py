# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        dic = {}
        for i in range(26):
            dic[chr(i + ord("a"))] = True
        for i in range(10):
            dic[str(i)] = True
        print(dic)
            
        s = s.lower()
        n = len(s)
        ans = ""
        for i in range(n):
            if s[i] in dic: 
                ans += s[i]
        
        return ans == ans[::-1]
            
