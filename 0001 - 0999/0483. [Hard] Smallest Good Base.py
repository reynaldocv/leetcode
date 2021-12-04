# https://leetcode.com/problems/smallest-good-base/

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def is_valid(base):
            ans = 0 
            for exp in range(length):
                ans += base**exp
            
            return n - ans

        n = int(n)
        N = len(bin(n)[2:])
        
        for length in range(N, 0, -1):
            start = 2
            end = n - 1
            while end - start >= 0:
                mid = (end + start) // 2
                v = is_valid(mid)
                if v < 0:
                    end = mid - 1
                elif v > 0:
                    start = mid + 1
                else:
                    return str(mid)
