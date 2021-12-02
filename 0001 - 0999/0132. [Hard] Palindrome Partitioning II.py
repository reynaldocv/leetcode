# https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def helper(word):
            if word == "":
                return 0 
            else: 
                ans = inf
                for i in range(1, len(word) + 1):
                    newWord = word[:i]
                    if newWord == newWord[::-1]:
                        ans = min(ans, 1 + helper(word[i:]))
                
                return ans
            
        return helper(s) - 1
            
        
