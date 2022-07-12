# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        counter = defaultdict(lambda: 0)
        tmp = 0
        counter[1] = 1
        
        for i in range(2, n + 1):
            tmp += counter[i - delay] - counter[i - forget]
            counter[i] = tmp % MOD
            
        ans = 0 
        
        for i in range(n, n - forget, -1):
            ans += counter[i]
            
        return ans % MOD
        
        
        
