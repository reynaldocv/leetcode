# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        start = -1
        arr = [i + 1 for i in range(n)]
        
        while len(arr)!= 1:
            arr.pop((start + k) % n)
            start = (start + k - 1) % n
            n -= 1
            if start == n: 
                start -= 1
        
        return arr[0]
        
