# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        
        m, n = len(words), len(words[0])
            
        l = len(target)
        
        dp = [1] + [0 for _ in range(l)]
        
        for i in range(n):
            count = collections.Counter(w[i] for w in words)
            
            for j in range(l - 1, -1, -1):
                dp[j + 1] += dp[j] * count[target[j]] % MOD
                
        return dp[-1] % MOD
        
class Solution2:
    def numWays(self, words: List[str], target: str) -> int:
        @cache
        def helper(i, idx):
            if l - i > n - idx:
                return 0 
            
            elif i == l: 
                return 1 
            
            else: 
                ans = helper(i, idx + 1)
                ans += counter[idx][target[i]]*helper(i + 1, idx + 1)
                
                return ans % MOD
            
        MOD = 10**9 + 7
        
        m, n = len(words), len(words[0])
        
        l = len(target)
        
        counter = defaultdict(lambda: defaultdict(lambda: 0))
        
        for word in words: 
            for (i, char) in enumerate(word):
                counter[i][char] += 1 
                
        return helper(0, 0)
