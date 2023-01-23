# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        follower = [0 for i in range(n)]
        followed = [0 for i in range(n)]
        
        for (a, b) in trust:
            follower[a - 1] += 1
            followed[b - 1] += 1
            
        for i in range(n):
            if follower[i] == 0 and followed[i] == n - 1:
                return i + 1
        return -1
                
        
