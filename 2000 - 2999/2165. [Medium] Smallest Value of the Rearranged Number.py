# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: 
            return 0 
        
        sign = 1 if num >= 0 else -1
        num = -num if num < 0 else num
        
        digits = [char for char in str(num) if char != "0"]
        zeros = sum(1 for char in str(num) if char == "0")
            
        if sign < 0: 
            arr =  sorted(digits, reverse = True) + ["0"]*zeros
        else:
            digits.sort()
            if zeros == 0: 
                arr =  digits
            else: 
                arr = [digits[0]] + ["0"]*zeros + digits[1:]
        
        return sign*int("".join(arr))
