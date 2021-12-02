# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(idx, mask):
            nonlocal ans
            if idx == n:
                ans += 1
            else: 
                for num in nums[idx]:
                    if (mask & 1 << num) >> num == 0: 
                        helper(idx + 1, mask ^ 1 << num)
            
        nums = [set() for _ in range(n)]
        
        for i in range(1, n + 1):
            for num in range(1, n + 1):
                if num % i == 0:
                    nums[i - 1].add(num)
                if i % num == 0: 
                    nums[i - 1].add(num)
        
        ans = 0 
        
        helper(0, 0)
        
        return ans
   
        
        
        
