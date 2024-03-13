# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0 
        right = n*(n + 1)//2
        
        for num in range(1, n + 1):
            left += num
            
            if left == right: 
                return num
            
            right -= num
            
        return -1
