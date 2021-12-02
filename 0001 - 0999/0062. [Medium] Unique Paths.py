# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1 for i in range(n)]
        for j in range(1, m):
            for i in range(1, n):
                arr[i] = arr[i - 1] + arr[i]
        
        return arr[n - 1]
        
