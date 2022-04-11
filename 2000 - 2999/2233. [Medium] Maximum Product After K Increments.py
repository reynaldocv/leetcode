# https://leetcode.com/problems/maximum-product-after-k-increments/

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        nums = sorted(nums) + [inf]
        n = len(nums)
        
        cnt = 1
        ans = 1
        
        for i in range(n - 1):
            a, b = nums[i + 1], nums[i]
            if a > b:
                if k > (a - b) * cnt:
                    k -= (a - b) * cnt                
                else:
                    div, mod = k // cnt, k % cnt
                    ans *= pow(b + div, cnt - mod, MOD)
                    ans *= pow(b + div + 1, mod, MOD)
                    k = 0                            
                    
            if k <= 0:
                break
            
            cnt += 1        
        j = i + 1
        
        while j < n - 1:
            ans = (ans * nums[j]) % MOD
            j += 1
            
        return ans % MOD
        

                
        
