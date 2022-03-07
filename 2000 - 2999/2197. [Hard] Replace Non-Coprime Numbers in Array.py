# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        prev = nums[0]
        ans = []
        
        for num in nums[1:] + [1]:            
            if gcd(prev, num) == 1: 
                ans.append(prev)
                prev = num
            else: 
                prev = lcm(prev, num)
                while ans and gcd(ans[-1], prev) > 1: 
                    prev = lcm(prev, ans.pop())
                    
        return ans 
