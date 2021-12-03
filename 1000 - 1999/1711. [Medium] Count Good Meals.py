# https://leetcode.com/problems/count-good-meals/

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        
        count = defaultdict(lambda: 0)
        
        for elem in deliciousness: 
            count[elem] += 1
            
        ans = 0
        for i in range(int(log(max(deliciousness), 2)) + 3):
            val = 2**i
            for key in count:
                if (val - key) in count: 
                    if key == val - key:
                        ans += count[key]*(count[key] - 1)//2
                    else: 
                        ans += count[key]*count[val - key]/2
            
        return int(ans) % MOD
                
            
        
