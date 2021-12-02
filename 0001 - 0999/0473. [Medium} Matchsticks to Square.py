# https://leetcode.com/problems/matchsticks-to-square/

class Solution:
    def makesquare(self, nums):
        def helper(idx):
            if idx == n: 
                return sides[0] == sides[1] == sides[2] == side
                
            else: 
                for i in range(4):
                    if sides[i] + nums[idx] <= side: 
                        sides[i] += nums[idx]
                        if helper(idx + 1):
                            return True
                        sides[i] -= nums[idx]
                
            return False
        
        if not nums:
            return False
        
        n = len(nums)

        perimeter = sum(nums)
        
        if perimeter % 4 != 0: 
            return False 
        
        side = perimeter // 4

        nums.sort(reverse = True)

        sides = [0 for _ in range(4)]

        return helper(0)
     
            
            
