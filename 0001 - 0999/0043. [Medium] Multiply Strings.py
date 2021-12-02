# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:        
        def add(num1, num2):        
            n = max(len(num1), len(num2))
            ans = [0]*n
            aux = 0
            for i in range(n):
                dig1 = num1[i] if i < len(num1) else 0
                dig2 = num2[i] if i < len(num2) else 0
                r = dig1 + dig2 + aux
                ans[i] = r % 10
                aux = r//10
            if aux > 0: 
                ans.append(aux)
            return ans
        
        def mul(num1, dig):
            n = len(num1)
            aux = 0
            ans = [0]*n
            for i in range(n):
                r = num1[i] * dig + aux
                ans[i] = r % 10
                aux = r//10
            if aux > 0: 
                ans.append(aux)
            return ans
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1 = [int(i) for i in num1[::-1]]
        num2 = [int(i) for i in num2[::-1]]
                
        ans = [0]
        for i in range(len(num2)):
            r = mul(num1, num2[i])
            for j in range(i):
                r.insert(0, 0)
            ans = add(ans, r)
        
        ans = [str(i) for i in ans[::-1]]
        return "".join(ans)
            
                
