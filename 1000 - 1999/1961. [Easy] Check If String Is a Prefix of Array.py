# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        tmp = ""
        
        for word in words: 
            tmp += word
            
            if tmp == s: 
                return True 
            
            if len(tmp) > len(s):
                break
        
        return False 
