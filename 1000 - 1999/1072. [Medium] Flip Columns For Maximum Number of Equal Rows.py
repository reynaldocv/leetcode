# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/ 

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        counter = defaultdict(lambda: 0)
        
        ans = 0 
              
        for row in matrix: 
            tmp1 = tuple([elem for elem in row])
            tmp2 = tuple([1 - elem for elem in row])
            
            counter[tmp1] += 1 
            counter[tmp2] += 1 
            
            ans = max(ans, counter[tmp1], counter[tmp2])
            
        return ans 
            
        
            
