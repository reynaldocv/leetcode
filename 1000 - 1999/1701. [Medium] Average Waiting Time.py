# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        last = customers[0][0]
        n = len(customers)
        ans = 0 
        
        for i in range(n):
            if last > customers[i][0]:
                last += customers[i][1]
                ans += last - customers[i][0]
            else: 
                last = customers[i][0] + customers[i][1]
                ans += customers[i][1]
            
        return ans/n
        
