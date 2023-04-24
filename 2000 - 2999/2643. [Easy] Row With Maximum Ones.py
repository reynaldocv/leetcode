# https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = (-1, -1)
        
        for (i, row) in enumerate(mat):
            ans = max(ans, (sum(row), -i))
            
        return (-ans[1], ans[0])
        
