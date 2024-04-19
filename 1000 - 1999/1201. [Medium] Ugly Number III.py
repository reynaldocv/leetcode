# https://leetcode.com/problems/ugly-number-iii/

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def helper(value):
            ans = 0 
            
            for i in range(1, 4):
                for comb in combinations(arr, i):
                    mcm = 1 
                    
                    for num in comb: 
                        mcm = lcm(mcm, num)
                    
                    ans += (-1)**(i + 1)*(value//mcm)
            
            return ans 
            
        arr = [a, b, c]
        
        start = 0 
        end = n*a 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) < n: 
                start = mid 
                
            else: 
                end = mid 
                
        return end 
        
        
