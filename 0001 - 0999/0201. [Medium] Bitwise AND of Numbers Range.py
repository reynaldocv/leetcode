# https://leetcode.com/problems/bitwise-and-of-numbers-range/ 

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0: 
            return 0 
        else:
            ans = 0
            while left > 0: 
                i = int(log(left, 2))
                commonBit = 0
                if 2**i <= right <= 2**(i + 1) - 1:
                    commonBit = 1 << i
                else: 
                    break
                ans += commonBit
                left -= commonBit
                right -= commonBit
            
            return ans
        
class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1
        
        return left << count
        
