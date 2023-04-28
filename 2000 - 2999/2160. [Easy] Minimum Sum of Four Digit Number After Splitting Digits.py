# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        arr = [int(char) for char in str(num)]  
        
        ans = inf
        
        for perm in permutations(arr, 4):
            ans = min(ans, perm[0] + 100*perm[1] + 10*perm[2] + perm[3])
            ans = min(ans, 10*perm[0] + perm[1] + 10*perm[2] + perm[3])
            
        return ans
