# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(start, end):
            if start > end: 
                return True 
            
            elif s[start] == s[end]:
                return helper(start + 1, end - 1)
            
            else: 
                tmp = s[start: end]
                
                if tmp == tmp[:: -1]:
                    return True 
                
                tmp = s[start + 1: end + 1]
                
                if tmp == tmp[:: -1]:
                    return True 
                
                return False 
            
        n = len(s)
        
        return helper(0, n - 1)
                
                
