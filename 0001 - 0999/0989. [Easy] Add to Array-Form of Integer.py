# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = int("".join(str(digit) for digit in num)) + k 
        
        return [int(char) for char in str(ans)]

class Solution2:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 = num[:: -1]
        num2 = [int(digit) for digit in str(k)][:: -1]
        
        m, n = len(num1), len(num2)
        
        aux = 0
        
        ans = []
        
        limit = max(m, n)
        
        for i in range(limit):
            bit1 = num1[i] if i < m else 0 
            bit2 = num2[i] if i < n else 0 
            
            bit = bit1 + bit2 + aux
            
            ans.append(bit % 10)
            
            aux = bit // 10
            
        if aux: 
            ans.append(1)
                    
        return ans[:: -1]
        
