# https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if m*n != l: 
            return []
        
        ans = []
        for i in range(m):
            ans.append(list(original[i*n: (i + 1)*n]))
        
        return ans
