# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        arr = [0, 1, 1]
        
        num1, num2 = 1, 1
        
        while num1 < 10**9: 
            num1 = num1 + num2
            num2 = num1 - num2
            
            arr.append(num1)
            
        ans = 0 
        
        while k > 0: 
            idx = bisect_right(arr, k) 
            
            k -= arr[idx - 1]
            
            ans += 1
        
        return ans 
        
        
        
