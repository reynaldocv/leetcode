# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        coins.sort()
        
        for coin in coins: 
            if ans < coin: 
                break 
            ans += coin
            
        return ans
        
