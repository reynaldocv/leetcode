# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for (j, bit) in enumerate(image[i][:: -1]):
                ans[i][j] = 1 - bit
                
        return ans
        
