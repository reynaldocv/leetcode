# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/ 

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def helper(row):
            ans = 0 
            for (i, bit) in enumerate(row[::-1]):
                ans += bit*2**i
                
            return ans
        
        m = len(matrix[0])
        counter = defaultdict(lambda: 0)        
        ans = 0
        
        for row in matrix: 
            val1 = helper(row)
            val2 = 2**m - 1 - val1
            counter[val1] += 1 
            counter[val2] += 1 
            
            ans = max(ans, counter[val1] + counter[val2])
            
        return ans//2
