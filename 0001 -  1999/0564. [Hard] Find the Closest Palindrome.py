# https://leetcode.com/problems/find-the-closest-palindrome/

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def helper(middle):
            m = len(middle)
            val = int(middle[:l//2]) if m % 2 == 0 else int(middle[:l//2 + 1])
            
            if m % 2 == 0: 
                if len(str(val - 1)) == len(str(val)):
                    start = str(val - 1) + str(val - 1)[::-1]
                else: 
                    start = str(val - 1) + "9" + str(val - 1)[::-1]
                
                if len(str(val + 1)) == len(str(val)):
                    end = str(val + 1) + str(val + 1)[::-1]
                else: 
                    end = str(val + 1) + str(val + 1)[:l//2][::-1]
                    
            else: 
                if len(str(val - 1)) == len(str(val)):
                    start = str(val - 1) + str(val - 1)[:l//2][::-1]
                else: 
                    start = str(val - 1) + str(val - 1)[::-1]
                
                if len(str(val + 1)) == len(str(val)):
                    end = str(val + 1) + str(val + 1)[:l//2][::-1]
                else: 
                    end = str(val + 1) + str(val + 1)[:l//2][::-1]
                    
            return (start, end)
        
        l = len(n)
        if int(n) <= 10: 
            return str(int(n) - 1)
        elif int(n) == 11: 
            return "9"
        
        if l % 2 == 0: 
            aux = n[:l//2]
            middle = aux + aux[::-1]
        else: 
            aux = n[:l//2 + 1]
            middle = aux + aux[:l//2][::-1]
            
        ans = (inf, inf)
        (start, end) = helper(middle)
        
        for i in [start, end, middle]:
            if i != n: 
                ans = min(ans, (abs(int(i) - int(n)), int(i)))
                
        return str(ans[1])
                
        
        
            
            
            
            
      
            
        
