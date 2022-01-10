# https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        twice = False
        while a > 0 or b > 0: 
            if twice: 
                if ans[-1] == "a":
                    ans += "b"
                    b -= 1
                else: 
                    ans += "a"
                    a -= 1                
                twice = False
            else:
                if a > b:
                    twice = True if ans and ans[-1] == "a" else False
                    ans += "a"
                    a -= 1
                    
                else: 
                    twice = True if ans and ans[-1] == "b" else False
                    ans += "b"
                    b -= 1 
                    
        return ans
                

                    
