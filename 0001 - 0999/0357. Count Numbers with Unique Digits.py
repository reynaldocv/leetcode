# https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def helper(num, cnt):
            if cnt == 0: 
                return 1
            
            else: 
                return num*helper(num - 1, cnt - 1)
            
        arr = [1]
        
        for i in range(1, n + 1):
            arr.append(9*helper(9, i - 1))
            
        return sum(arr)
            
            
