# https://leetcode.com/problems/abbreviating-the-product-of-a-range/

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        MAX = 10**12
        prefix, suffix, zero = 1, 1, 0
        
        for num in range(left, right + 1):
            prefix *= num  
            suffix *= num  
            while suffix % 10 == 0:  
                zero += 1
                suffix //= 10
                
            if suffix > MAX:  
                suffix %= MAX
                
            while prefix > MAX:  
                prefix //= 10
                
        if suffix < 10**10:
            return str(suffix) + 'e' + str(zero)
        else:
            return str(prefix)[:5] + '...' + str(suffix)[-5:] + 'e' + str(zero)
