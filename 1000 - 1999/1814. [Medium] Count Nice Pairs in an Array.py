# https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        counter = defaultdict(lambda: 0)
        
        ans = 0
        
        for num in nums: 
            delta = num - int(str(num)[::-1])
            
            ans = (ans + counter[delta]) % MOD 
            
            counter[delta] += 1
        
        return ans 
