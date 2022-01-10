# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def helper(arr):
            ans = set()
            for num in arr: 
                units = num % 10 
                if units + k < 10:
                    ans.add(num*10 + units + k)
                if units - k >= 0:
                    ans.add(num*10 + units - k)
            
            return ans
           
        ans = [i for i in range(1, 10)]
        
        for _ in range(n - 1):
            ans = helper(ans)
            
        return ans
        
            
