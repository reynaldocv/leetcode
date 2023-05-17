# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        seen = {num for num in banned}
        
        aSum = 0
        
        ans = 0 
        
        for i in range(1, n + 1):
            if i not in seen: 
                if aSum  + i <= maxSum: 
                    aSum += i 
                    
                    ans += 1 
                    
        return ans 
                
