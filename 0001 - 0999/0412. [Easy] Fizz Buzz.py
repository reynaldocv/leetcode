# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0: 
                tmp = ""
                if num % 3 == 0:
                    tmp += "Fizz"
                if num % 5 == 0: 
                    tmp += "Buzz"
        
                ans.append(tmp)
            
            else: 
                ans.append(str(num))
                
        return ans 
            
