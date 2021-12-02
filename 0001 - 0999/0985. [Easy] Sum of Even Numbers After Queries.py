# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        n = len(A)
        ans = []
        s = sum([x if (x % 2 == 0) else 0 for x in A])
        for (a, b) in queries:
            x0 = A[b]
            A[b] += a
            x1 = A[b]
            if x0 % 2 == 0: 
                s -= x0
            if x1 % 2 == 0:
                s += x1
            ans.append(s)
        return ans
