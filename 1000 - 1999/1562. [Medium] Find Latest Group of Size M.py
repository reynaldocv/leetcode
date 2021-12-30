# https://leetcode.com/problems/find-latest-group-of-size-m/
  
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        
        if m == n:
            return m
        
        dp = [0 for _ in range(n + 2)]        
        ans = -1
        
        for i , a in enumerate(arr):            
            left , right = dp[a - 1] , dp[a + 1]                         
            if left == m or right == m:
                ans = i
                
            dp[a - left] = dp[a + right] = left + right + 1
            
        return ans
        
class Solution2:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        stack = [(1, n)]
        
        if n == m: 
            return n
        
        ans = n - 1 
        for num in arr[::-1]:
            idx = bisect_left(stack, (num, inf))
            idx -= 1
            (a, b) = stack.pop(idx)
            if a == num: 
                if b - num == m: 
                    return ans
                insort(stack, (a + 1, b))
            elif b == num: 
                if num - a == m: 
                    return ans
                insort(stack, (a, b - 1))
            else: 
                if b - num == m or num - a == m: 
                    return ans
                insort(stack, (a, num - 1))
                insort(stack, (num + 1, b))
            
            ans -= 1
                
        return -1
