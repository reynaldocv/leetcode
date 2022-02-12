# https://leetcode.com/problems/count-different-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        @cache
        def helper(start, end):
            if start == end: 
                return 0 
            else: 
                ans = 0 
                for char in "abcd":
                    idx1 = bisect_left(index[char], start)
                    idx2 = bisect_left(index[char], end) - 1
                    if idx1 <= idx2 < len(index[char]):
                        if start <= index[char][idx1] < end: 
                            ans += 1 
                            if idx1 < idx2: 
                                ans += 1 + helper(index[char][idx1] + 1, index[char][idx2])
                
                return ans     
        
        MOD = 10**9 + 7
        
        index = defaultdict(lambda: [])
        n = len(s)
        
        for (i, char) in enumerate(s):
            index[char].append(i)
        
        return helper(0, n) % MOD 
