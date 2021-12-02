# https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4: return False
        arr = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i, n + 1, i):
                arr[j] += 1
        print(arr)
        return True if arr[n] == 3 else False
