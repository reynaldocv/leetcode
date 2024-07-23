# https://leetcode.com/problems/find-latest-group-of-size-m/
  
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        
        if m == n:
            return m
        
        dp = [0 for _ in range(n + 2)]     
        
        ans = -1 
        
        for (ith, num) in enumerate(arr):
            left = dp[num - 1]
            right = dp[num + 1]
            
            if left == m or right == m: 
                ans = ith 
                
            total = left + 1 + right            
                
            dp[num - left] = total
            dp[num + right] = total
            
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
