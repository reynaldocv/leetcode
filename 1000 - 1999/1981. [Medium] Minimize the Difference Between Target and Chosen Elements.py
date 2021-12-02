# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        nums = {0}
        n = len(mat)
        for i in range(n):
            nums = {num + val for num in nums for val in mat[i]}        
        ans = min([abs(num - target) for num in nums])
        
        return ans
        
