# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ans1 = [0]*n
        ans2 = [0]*n
        aux = 0
        for i in range(n):
            if s[i] == "0":
                aux += 1
            ans1[i] = aux
        aux = 0
        for i in range(n-1, -1, -1):
            if s[i] == "1":
                aux += 1
            ans2[i] = aux
            
        ans = 0
        for i in range(n - 1):
            ans = max(ans, ans1[i] + ans2[i + 1])
        return ans
            
        
