# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [x**2 for x in A]
        ans.sort()
        return ans
        
