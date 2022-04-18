# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k: 
            aux = ""
            for i in range(len(s)//k + 1):
                value = s[k*i: k*(i + 1)]
                aSum = 0
                go = False
                for val in value: 
                    go = True
                    aSum += int(val)
                    
                if go: 
                    aux += str(aSum)
                
            s = aux
            
        return s 
                    
        
