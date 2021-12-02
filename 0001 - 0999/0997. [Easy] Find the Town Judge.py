# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr1 = [0 for i in range(n)]
        arr2 = [0 for i in range(n)]
        for (a, b) in trust:
            arr1[a - 1] += 1
            arr2[b - 1] += 1
            
        for i in range(n):
            if arr1[i] == 0 and arr2[i] == n - 1:
                return i + 1
        return -1
