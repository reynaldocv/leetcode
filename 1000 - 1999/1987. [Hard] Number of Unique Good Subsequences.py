# https://leetcode.com/problems/number-of-unique-good-subsequences/

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        dp = [1]
        last = {}
        
        for (i, char) in enumerate(binary):
            aux = 2*dp[-1]
            if char in last: 
                aux -= dp[last[char]]
            elif char == "0":
                aux -= 1
            
            last[char] = i
            dp.append(aux)
            
        return (dp[-1] - 1 + ("0" in binary)) % MOD
