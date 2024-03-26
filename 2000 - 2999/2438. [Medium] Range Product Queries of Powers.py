# https://leetcode.com/problems/range-product-queries-of-powers/

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        arr = []
        i = 0
        
        while n > 0: 
            bit = n % 2
            
            if bit != 0: 
                arr.append(bit*2**i)
                
            n //= 2
            i += 1 
            
        mult = [1]
        
        for num in arr: 
            mult.append(mult[-1]*num)
            
        ans = []
        
        for (start, end) in queries: 
            inv = pow(mult[start], -1, MOD)  
            
            ans.append((mult[end + 1]*inv) % MOD)
            
        return ans 
            
            
