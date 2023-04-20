# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def helper(number):
            ans = 0 
            
            while number: 
                ans += (number % 10)
                
                number //= 10 
                
            return ans 
        
        counter = defaultdict(lambda: 0)
        
        ans = 0 
        
        for num in range(lowLimit, highLimit + 1):
            box = helper(num)
            
            counter[box] += 1 
            
            ans = max(ans, counter[box])
            
        return ans 
