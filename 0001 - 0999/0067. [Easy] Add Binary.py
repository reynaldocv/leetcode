# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def ChangeBase(n, k, j):
            if n <= 0: 
                return 0
            else: 
                return (n % j) + k*ChangeBase(n//j, k, j) 
            
        
        auxa = ChangeBase(int(a), 2, 10)  
        auxb = ChangeBase(int(b), 2, 10)    
        
        return str(ChangeBase(auxa + auxb, 10, 2))
