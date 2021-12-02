# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        increasing = [0]*n
        decreasing = [0]*n
        ans = 0
        for i in range(n):
            for j in range(i):
                if rating[i] > rating[j]:
                    decreasing[i] += 1
                    ans += decreasing[j]
                else: 
                    increasing[i] += 1
                    ans += increasing[j]
        
        return ans
