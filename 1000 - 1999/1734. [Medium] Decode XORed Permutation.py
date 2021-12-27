# https://leetcode.com/problems/decode-xored-permutation/

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:        
        n = len(encoded) + 1
        val = 0
        for i in range(1, n, 2):
            val ^= encoded[i]
        
        for num in [0^val, 1^val]:
            i = 0 
            seen = {num: True}
            ans = [num]
            while 1 <= num < n + 1  and i < n - 1:                 
                num = num ^ encoded[i]
                if num in seen or num == 0: 
                    break
                else: 
                    i += 1
                    seen[num] = True
                    ans.append(num)
            
            if len(ans) == n: 
                return ans
