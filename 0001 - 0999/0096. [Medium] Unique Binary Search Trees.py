# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        ans = [0 for i in range(n + 1)]
        ans[0] = ans[1] = 1
        for k in range(2, n + 1):
            aux = 0
            for j in range(0, k):
                aux += ans[j]*ans[k - 1 - j]
            ans[k] = aux
        
        return ans[n]
