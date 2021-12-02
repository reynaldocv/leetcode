# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        def sumDigits(n):
            if n <= 0: return 0
            return  (n % 10) + sumDigits(n//10)
        
        box = {}
        for i in range(lowLimit, highLimit + 1):
            aux = sumDigits(i)
            box[aux] = box.get(aux, 0) + 1
            
        print(box)
        ans = 0
        for i in box: 
            ans = max(ans, box[i]) 
            
        return ans
        
