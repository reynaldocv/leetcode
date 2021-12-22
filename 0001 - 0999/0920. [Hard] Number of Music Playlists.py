# https://leetcode.com/problems/number-of-music-playlists/solution/

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def helper(i, j):
            if i == 0: 
                return j == 0
            
            ans = helper(i - 1, j - 1)*(n - j + 1)
            ans += helper(i - 1, j)*max(j - k, 0)
            
            return ans % MOD
        
        MOD = 10**9 + 7
        
        return helper(goal, n)
        
