# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        S = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                S[i][j] = matrix[i - 1][j - 1] + S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1]

        ans = 0 
        for i1 in range(1, n + 1):
            for i2 in range(i1):
                counter = defaultdict(lambda: 0)
                counter[0] = 1
                for j in range(1, m + 1):
                    s = S[i1][j] - S[i2][j]
                    ans += counter[s - target]
                    counter[s] += 1
        return ans
