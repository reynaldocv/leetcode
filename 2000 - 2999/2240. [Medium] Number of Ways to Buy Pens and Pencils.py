# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0 
        for i in range(total//cost1 + 1):
            aux = total - cost1*i
            ans += aux//cost2 + 1
            
        return ans 
            
