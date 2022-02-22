# https://leetcode.com/problems/image-overlap/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def helper(xShift, yShift, arr1, arr2):
            aux1, aux2 = 0, 0 
            for (row1, row2) in enumerate(range(yShift, n)):
                for (col1, col2) in enumerate(range(xShift, n)):
                    if arr1[row2][col2] == arr2[row1][col1] == 1: 
                        aux1 += 1 
                    if arr1[row2][col1] == arr2[row1][col2] == 1: 
                        aux2 += 1 
                        
            return max(aux1, aux2)
        
        n = len(img1)
        
        ans = 0 
        
        for yShift in range(n):
            for xShift in range(n):
                ans = max(ans, helper(xShift, yShift, img1, img2))
                ans = max(ans, helper(xShift, yShift, img2, img1))
                
        return ans 
