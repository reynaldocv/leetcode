# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[:: -1], num2[:: -1]
        
        m, n = len(num1), len(num2)        
        limit = max(m, n)
        
        ans = ""
        
        aux = 0 
        
        for i in range(limit):
            val1 = int(num1[i]) if i < m else 0 
            val2 = int(num2[i]) if i < n else 0 
            
            aSum = val1 + val2 + aux
            
            aux = aSum // 10 
                        
            ans += str(aSum % 10)
            
        if aux: 
            ans += str(1)
            
        return ans[:: -1]
            
