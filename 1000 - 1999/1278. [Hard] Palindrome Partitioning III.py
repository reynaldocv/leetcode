# https://leetcode.com/problems/palindrome-partitioning-iii/

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @cache
        def cost(i, j):
            if i >= j: 
                return 0 
            else: 
                return cost(i + 1,j - 1) + (s[i] != s[j])
        
        n = len(s)
        
        ans = [cost(i, n - 1) for i in range(n)]
        
        for j in range(k - 1):
            for i in range(n - j - 1):   
                ans[i] = inf
                for l in range(i, n - j - 1):
                    ans[i] = min(ans[i], cost(i, l) + ans[l + 1])
                
        return ans[0]
