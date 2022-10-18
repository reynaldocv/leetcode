# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        
        for i in range(n - 1):
            cnt = 0 
            prev = ""
            
            newString = ""
            
            for char in ans + "$":
                if char == prev: 
                    cnt += 1 
                    
                else: 
                    if prev != "":
                        newString += str(cnt) + prev
                        
                    prev = char
                    cnt = 1
            
            ans = newString
            
        return ans
        
