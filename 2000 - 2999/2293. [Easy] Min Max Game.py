# https://leetcode.com/problems/min-max-game/

class Solution:
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def helper(arr):
            ans = []
                
            turn = True 
            
            while arr: 
                num1 = arr.pop(0)
                num2 = arr.pop(0)
                
                if turn:                 
                    ans.append(min(num1, num2))
                    
                else: 
                    ans.append(max(num1, num2))
                
                turn = not turn
                    
            return ans 
        
        while len(nums) > 1: 
            nums = helper(nums)
            
        return nums.pop()
                
            
