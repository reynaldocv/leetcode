# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort(reverse = True)
        aSum = sum(beans)
            
        ans = inf
        
        for (i, bean) in enumerate(beans):
            ans = min(ans, aSum - (i + 1)*bean)
            
        return ans
