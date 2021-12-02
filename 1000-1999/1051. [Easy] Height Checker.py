# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        aux = heights.copy()
        aux.sort()
        ans = 0
        l = len(heights)
        for i in range(l):
            if heights[i] != aux[i]:
                ans += 1
        return ans
        
