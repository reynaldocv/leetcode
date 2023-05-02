# https://leetcode.com/problems/strong-password-checker-ii/

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        
        index = {}
        
        for i in range(26):
            index[chr(ord("a") + i)] = 0 
            index[chr(ord("A") + i)] = 1
            
        for i in range(10):
            index[str(i)] = 2 
            
        for char in "!@#$%^&*()-+":
            index[char] = 3 
            
        counter = (0, )*4
        
        for (i, char) in enumerate(password):
            idx = index[char]
            
            counter = counter[: idx] + (1, ) + counter[idx + 1: ]
            
            if i < n - 1 and char == password[i + 1]:
                return False 
            
        return sum(counter) == 4 and n > 7
                
          
