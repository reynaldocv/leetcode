# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        
        ans = 0
        for i in range(n - 1):
            xor = arr[i]
            for j in range(i + 1, n):
                xor ^= arr[j]
                if xor == 0: 
                    ans += (j - i)
                    
        return ans
        
