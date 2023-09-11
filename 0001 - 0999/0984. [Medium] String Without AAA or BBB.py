# https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        
        while a > 0 or b > 0:             
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = (ans[-1] == "b")
                
            else: 
                writeA = (a >= b)
                
            if writeA: 
                ans += "a"
                
                a -= 1
            else: 
                ans += "b"
                
                b -= 1 
           
        return ans
                    
