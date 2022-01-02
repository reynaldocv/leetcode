# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        @cache
        def helper(string):
            ans = 0 
            for char in string: 
                if char == "1":
                    ans += 1 
            
            return ans
        
        arr = [helper(row) for row in bank if helper(row) != 0]
        n = len(arr)
        
        if n <= 1: 
            return 0 
        
        ans = 0 
        for i in range(n - 1):
            ans  += arr[i]*arr[i + 1]
            
        return ans
            
        
