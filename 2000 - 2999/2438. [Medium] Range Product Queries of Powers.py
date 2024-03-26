# https://leetcode.com/problems/range-product-queries-of-powers/

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7 
        
        base = 1
        
        while n >= base: 
            base *= 2 
            
        base //= 2 
        arr = []
        
        while n > 0: 
            if n >= base: 
                arr.insert(0, base)
                
                n -= base
                
            base //= 2             
            
        mult = [1]
        
        for num in arr: 
            mult.append(mult[-1]*num)
            
        ans = []
        
        for (start, end) in queries: 
            inv = pow(mult[start], -1, MOD)  
            
            ans.append((mult[end + 1]*inv) % MOD)
            
        return ans 
            
