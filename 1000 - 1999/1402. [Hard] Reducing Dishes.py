# https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        
        satisfaction.sort()
        
        ans = 0
        
        for (i, num) in enumerate(satisfaction):
            ans += (i + 1)*num
        
        tmp = ans
        
        right = [num for num in satisfaction]
        
        for i in range(n - 2, -1, -1):
            right[i] += right[i + 1]            
            
        for i in range(n):
            tmp -= right[i]
            
            ans = max(ans, tmp)
            
        return ans 

class Solution2:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = 0 
        
        total = 0
                
        satisfaction.sort()
        
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            
            ans += total
            
        return ans
                    
            
        
            
            
