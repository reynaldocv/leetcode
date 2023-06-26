# https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                first = int(str(nums[i])[0])
                last = int(str(nums[j])[-1])
                
                if gcd(first, last) == 1: 
                    ans += 1 
                    
        return ans 
                
                
        
