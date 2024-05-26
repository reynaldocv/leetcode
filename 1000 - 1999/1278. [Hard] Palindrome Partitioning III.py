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

class Solution2:
    def palindromePartition(self, s: str, k: int) -> int:
        def collaborator(word):
            start = 0 
            end = len(word) - 1
            
            ans = 0 
            
            while start < end:
                if word[start] != word[end]:
                    ans += 1 
                
                start += 1 
                end -= 1 
                
            return ans 
        
        @cache
        def helper(idx, k):
            if k == 1: 
                return collaborator(s[idx: ])
            
            else: 
                tmp = ""
                ans = inf
                
                for i in range(idx, n - k + 1):
                    tmp += s[i]
                    
                    ans = min(ans, collaborator(tmp) + helper(i + 1, k - 1))
                    
                return ans
            
        n = len(s)
            
        return helper(0, k)
         
