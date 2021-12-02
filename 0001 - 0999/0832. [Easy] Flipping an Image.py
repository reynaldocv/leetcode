# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = [x[::-1] for x in A]
        l = len(ans)
        for i in range(l):
            for j in range(l):
                ans[i][j] = (ans[i][j] + 1) % 2
        return ans
        
