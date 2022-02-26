# https://leetcode.com/problems/adding-two-negabinary-numbers/

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def helper(arr):
            n = len(arr)
            ans = 0 
            for (i, val) in enumerate(arr):
                ans += val*(-2)**(n - 1 - i)
                
            return ans
        
        def collaborator(num):
            ans = []
            while num != 0:
                if num % 2 != 0:
                    ans.insert(0, 1)
                    num = (num - 1)//-2
                else:
                    ans.insert(0, 0)
                    num = num//-2

            return ans if ans else [0]
        
        num1 = helper(arr1)
        num2 = helper(arr2)
        
        return collaborator(num1 + num2)
