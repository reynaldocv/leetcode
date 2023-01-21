# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def helper(num):
            tmp = num 
            
            while tmp > 0:
                unit = tmp % 10
                
                if unit == 0 or num % unit != 0: 
                    return False 
                
                tmp = tmp // 10 
                
            return True 
        
        ans = []
        
        for num in range(left, right + 1):
            if helper(num):
                ans.append(num)
                
        return ans
