# https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def helper(word):
            if word.isdigit():
                if len(word) == len(str(int(word))):
                    if 0 <= int(word) <= 255: 
                        return True 
                    
            return False 
        
        def collaborator(word):
            if 1<= len(word) <= 4: 
                return all([char in "0123456789abcdefABCDEF" for char in word])
            
            return False 
            
        if "." in queryIP:
            arr = queryIP.split(".")
            
            if len(arr) == 4: 
                if all([helper(word) for word in arr]):
                    return "IPv4"
                        
        else: 
            arr = queryIP.split(":")
        
            if len(arr) == 8: 
                if all([collaborator(word) for word in arr]):
                    return "IPv6"
            
        return "Neither"
            
            
            
            
            
            
