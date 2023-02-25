# https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def helper(num):
            ans = 0 
            
            while num: 
                ans += (num % 10)
                
                num //= 10 
                
            return ans 
        
        ans = 0 
        
        maxLen = 0 
        
        counter = defaultdict(lambda: 0)
        
        for num in range(1, n + 1):
            sumDigits = helper(num)
            
            counter[sumDigits] += 1 
            
            if counter[sumDigits] == maxLen: 
                ans += 1 
                
            elif counter[sumDigits] > maxLen: 
                maxLen = counter[sumDigits]
                
                ans = 1 
                
        return ans 
