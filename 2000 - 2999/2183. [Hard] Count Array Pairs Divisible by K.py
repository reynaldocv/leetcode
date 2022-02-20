# https://leetcode.com/problems/count-array-pairs-divisible-by-k/

class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:        
        factors = []
        limit = int(k**.5)
        
        for num in range(1, limit + 1):
            if k % num == 0: 
                factors.append(num)
                
        ans = 0 
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            common = gcd(num, k)
            ans += counter[k//common]
            vals = set()
            for factor in factors: 
                if common % factor == 0: 
                    vals.add(factor)
                    vals.add(common//factor)
                    
            for val in vals: 
                counter[val] += 1 
                
        return ans
