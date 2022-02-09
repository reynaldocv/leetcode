# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        right = [0]
        prev = 0 
        for i in range(n - 1, -1, -1):
            if grumpy[i] == 0: 
                prev += customers[i]
            
            right.insert(0, prev)
        
        ans = 0         
        left = 0 
        aSum = sum(customers[:minutes])
        
        for (i, customer) in enumerate(customers[minutes: ] + [0]):
            ans = max(ans, left + aSum + right[minutes + i])
            aSum += customer - customers[i]
            if grumpy[i] == 0: 
                left += customers[i]
        
        return ans
