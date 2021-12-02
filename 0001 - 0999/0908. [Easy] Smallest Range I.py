# https://leetcode.com/problems/smallest-range-i/

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_ = max(A)
        min_ = min(A)
        ans = max_ - min_ - 2*K
        return 0 if (ans < 0) else ans
        
