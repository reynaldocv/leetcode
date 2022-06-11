# https://leetcode.com/problems/strong-password-checker-ii/

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        upper = {chr(ord("A") + i) for i in range(26)}
        lower = {chr(ord("a") + i) for i in range(26)}
        
        digits = {str(i) for i in range(10)}
        
        specials = "!@#$%^&*()-+"
        
        counter = (0, 0, 0, 0)
        
        for char in password: 
            if char in upper: 
                counter = (1, ) + counter[1: ]
            elif char in lower: 
                counter = counter[: 1] + (1, ) + counter[2: ]
            elif char in digits: 
                counter = counter[: 2] + (1, ) + counter[3: ]
            elif char in specials: 
                counter = counter[: 3] + (1, ) + counter[4: ]
            
        n = len(password)

        if sum(counter) >= 4 and n >= 8: 
            
            for i in range(n - 1):
                if password[i] == password[i + 1]:
                    return False 

            return True 
        
        return False 
