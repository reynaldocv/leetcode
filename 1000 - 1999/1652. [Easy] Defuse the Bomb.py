# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0]*n
        
        if k == 0: return ans
        if k > 0:
            for i in range(n):
                aux = 0
                for j in range(i + 1, i + 1 + k):
                    aux += code[(j + n) % n]
                ans[i] = aux
        else: 
            for i in range(n):
                aux = 0                
                for j in range(i + k, i ):                    
                    aux += code[(j + n) % n]
                ans[i] = aux
        return ans
