# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        text = ["Fizz", "Buzz", "FizzBuzz"]
        ans = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append(text[2])
            elif i % 3 == 0:
                ans.append(text[0])
            elif i % 5 == 0:
                ans.append(text[1])
            else:
                ans.append(str(i))
        
        return ans
            
