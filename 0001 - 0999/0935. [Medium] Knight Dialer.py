# https://leetcode.com/problems/knight-dialer/

class Solution:
    def knightDialer(self, n: int) -> int:        
        MOD = 10**9 + 7 
        
        graph = {}
        graph[0] = [4, 6]
        graph[1] = [6, 8]
        graph[2] = [7, 9]
        graph[3] = [4, 8]
        graph[4] = [3, 9, 0]
        graph[5] = []
        graph[6] = [1, 7, 0]
        graph[7] = [2, 6]
        graph[8] = [1, 3]
        graph[9] = [2, 4]
                    
        dp = [1 for _ in range(10)]
        
        for _ in range(n - 1):
            newDp = [0 for _ in range(10)]
            
            for u in range(10):
                for v in graph[u]:                
                    newDp[v] = (newDp[v] + dp[u]) % MOD 
                    
            dp = newDp
            
        return sum(dp) % MOD

class Solution2:
    def knightDialer(self, n: int) -> int:
        @cache
        def helper(u, n):
            if n == 1: 
                return 1 
            
            else: 
                ans = 0 
                
                for v in graph[u]:
                    ans = (ans + helper(v, n - 1)) % MOD 
                    
                return ans 
        
        MOD = 10**9 + 7 
        
        graph = {}
        graph[0] = [4, 6]
        graph[1] = [6, 8]
        graph[2] = [7, 9]
        graph[3] = [4, 8]
        graph[4] = [3, 9, 0]
        graph[5] = []
        graph[6] = [1, 7, 0]
        graph[7] = [2, 6]
        graph[8] = [1, 3]
        graph[9] = [2, 4]
                    
        ans = 0 
        
        for i in range(10):
            ans = (ans + helper(i, n)) % MOD 
            
        return ans 
                
