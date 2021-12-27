# https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        stack = [i for i in range(1, 10)]
        ans = []
        while stack: 
            num = stack.pop(0)
            if num % 10 != 9:
                num = num*10 + (num % 10) + 1
                if low <= num <= high:
                    ans.append(num)

                if num % 10 != 0 and num <= high:                     
                    stack.append(num)

        return ans
                
                
        
