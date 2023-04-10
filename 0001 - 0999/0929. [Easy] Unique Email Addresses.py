# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        
        for email in emails:             
            words = email.split("@")
            
            tmp = ""
            
            for char in words[0]:
                if char != ".":                    
                    if char == "+":
                        break
                    
                    else: 
                        tmp += char 
                        
            seen.add(tmp + "@" + words[1])
        
        return len(seen)
                
                
