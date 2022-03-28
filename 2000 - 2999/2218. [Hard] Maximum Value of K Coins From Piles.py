# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def helper(row, k):
            if row == n: 
                if k == 0: 
                    return 0 
                if k > 0: 
                    return -inf
            
            ans = helper(row + 1, k)
            left = 0 
            for i in range(min(k, len(piles[row]))):
                left += piles[row][i]
                ans = max(ans, left + helper(row + 1, k - i - 1))
                
            return ans
            
        n = len(piles)
        
        return helper(0, k)
