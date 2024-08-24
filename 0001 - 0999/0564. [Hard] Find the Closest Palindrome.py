# https://leetcode.com/problems/find-the-closest-palindrome/

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        
        if m == 1: 
            if n == 0:
                return "1"
            
            else: 
                return str(int(n) - 1)
        
        elif m % 2 == 0: 
            root = n[: m//2]
            
            _prev = str(int(root) - 1)
            _next = str(int(root) + 1)
            
            arr = [root + root[:: -1], _prev + _prev[:: -1], _next + _next[:: -1]]
            
            arr.append("9"*(m - 1))
            arr.append("1" + "0"*(m - 1) + "1")
        else:             
            root = n[: m//2 + 1]
            _prev = str(int(root) - 1)
            _next = str(int(root) + 1)
            
            arr = [root[: -1] + root[:: -1], _prev[: -1] + _prev[:: -1], _next[: -1] + _next[:: -1]]
            
            arr.append("9"*(m - 1))
            arr.append("1" + "0"*(m - 1) + "1")
            
        arr.sort(key = lambda item: (abs(int(item) - int(n)), int(item)))
        
        if arr[0] == n: 
            return arr[1]
        
        else: 
            return arr[0]
            
            
            
            
            
        
        
        
            
        
        
                
        
        
            
            
            
            
      
            
        
