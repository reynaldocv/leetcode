# https://leetcode.com/problems/count-good-meals/

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        
        count = defaultdict(lambda: 0)
        
        for elem in deliciousness: 
            count[elem] += 1
            
        limit = int(log(max(deliciousness), 2)) 
        
        ans = 0
        
        for i in range(limit + 3):
            val = 2**i
            
            for key in count:
                tmp = val - key
                
                if tmp in count: 
                    if key == tmp:
                        ans += count[key]*(count[key] - 1)
                        
                    else: 
                        ans += count[key]*count[tmp]
            
        return (ans//2) % MOD

        
