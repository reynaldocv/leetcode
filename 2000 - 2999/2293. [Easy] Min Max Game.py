# https://leetcode.com/problems/min-max-game/

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def helper(arr):
            n = len(arr)
            if n == 1: 
                return arr
            
            else:                     
                ans = []

                turn = True 

                for i in range(n//2):
                    if turn: 
                        ans.append(min(nums[2*i], nums[2*i + 1]))
                    else: 
                        ans.append(max(nums[2*i], nums[2*i + 1]))

                    turn = not turn 

                return ans 
            
        while len(nums) > 1: 
            nums = helper(nums)
            
        return nums[0]
            
