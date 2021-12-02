# https://leetcode.com/problems/count-the-repetitions/

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        dp = []
        n, m = len(s1), len(s2)
        
        for i in range(m):
            start = i
            cnt = 0
            for j in range(n):
                if s1[j] == s2[start]:
                    start += 1
                    if start == m:
                        start = 0
                        cnt += 1
            
            print(i, start, cnt)
            dp.append((start,cnt))
            
        ans = 0
        i = 0
        for _ in range(n1):
            ans += dp[i][1]
            i = dp[i][0]
            
        return ans // n2
        
