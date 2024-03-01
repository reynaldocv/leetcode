# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy) 
        
        total = [0]
        satisfied = [0]
        
        for (i, mood) in enumerate(grumpy):
            if mood == 0: 
                satisfied.append(satisfied[-1] + customers[i])
                
            else:
                satisfied.append(satisfied[-1])
                
            total.append(total[-1] + customers[i])
            
        ans = satisfied[-1]
        
        for i in range(1, n + 1):
            if i >= minutes: 
                left = satisfied[i - minutes]
                center = total[i] - total[i - minutes]
                right = satisfied[-1] - satisfied[i]
                
                ans = max(ans, left + center + right )
                
        return ans 
            
        
