# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(start, end):
            if start > end: 
                return 0 
            
            key = (start, end)
            if key in seen: 
                return seen[key]
            else:             
                if start == end: 
                    seen[(start, end)] = 1                    
                elif s[start] == s[end]:
                    seen[key] = 2 + helper(start + 1, end - 1)
                else: 
                    seen[key] = max(helper(start + 1, end), helper(start, end - 1))
                
                return seen[key]
        
        n = len(s)
        seen = {}
        return helper(0, n - 1)
