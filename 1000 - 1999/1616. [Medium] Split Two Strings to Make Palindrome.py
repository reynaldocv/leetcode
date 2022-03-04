# https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool: 
        def helper(string1, string2):
            start = 0 
            end = n - 1
            while string1[start] == string2[end]:
                start += 1 
                end -= 1 
                if start >= end: 
                    return True 
                
            aux1, aux3 = start, end 

            while string1[start] == string1[end]:
                start += 1 
                end -= 1 
                if start >= end: 
                    return True 
                
            start, end = aux1, aux3

            while string2[start] == string2[end]:
                start += 1 
                end -= 1 
                if start >= end: 
                    return True 
            
            return False 
        
        n = len(a)
        
        return helper(a, b) or helper(b, a)
            
        
