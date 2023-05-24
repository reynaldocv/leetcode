# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 32       
        
        counter = (0,)*(n + 1)
        
        sign = 0
        
        for num in nums: 
            if num > 0:             
                sign = (sign + 1) % 3
                
            elif num < 0: 
                sign = (sign - 1) % 3
                
            num = abs(num)
        
            position = 0 
            
            while num: 
                unit = num % 2 
                
                if unit == 1: 
                    counter = counter[: position] + ((counter[position] + 1) % 3, ) + counter[position + 1: ]
                
                num //= 2 
                
                position += 1 
                
        ans = 0
        
        for i in range(n + 1):
            ans += counter[i] << i
        
        if sign == 2: 
            ans *= -1
            
        return ans 
        
