# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 32       
        counter = (0,)*(n + 1)
        pos = 0
        for num in nums: 
            k = 0
            pos = (pos + 1) % 3 if num >= 0 else pos
            num = abs(num)
            while num > 0:
                if (num & 1 == 1):                    
                    counter = counter[:n - k] + ((counter[n - k] + 1) % 3,) + counter[n - k + 1:]                
                num = num >> 1
                k += 1
        ans = 0
        for i in range(n, -1, -1):
            ans += counter[i] << n - i
        
        return -ans if pos == 0 else ans
                
        
