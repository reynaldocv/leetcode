# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        if n == 1: return ans 
        
        for i in range(0, n - 1):
            aux = ""
            counter = 0 
            number = ""
            for i in ans: 
                if number != i: 
                    if number != "":                    
                        aux = aux + str(counter) + number
                    counter = 1
                    number = i                    
                else: 
                    counter += 1
            aux = aux + str(counter) + number            
            ans = aux
        return ans
        
