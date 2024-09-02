# https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [str(num1), str(num2), str(num3)]
        
        for i in range(3):
            while len(nums[i]) < 4: 
                nums[i] = "0" + nums[i]
                
        ans = ""
        
        for i in range(4):
            ans += min(nums[0][i], nums[1][i], nums[2][i])
            
        return int(ans)
        
