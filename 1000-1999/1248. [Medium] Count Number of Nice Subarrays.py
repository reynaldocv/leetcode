# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        position = {0: -1}
        i = 1
        n = len(nums)
        for (pos, num) in enumerate(nums):
            if num % 2 == 1: 
                position[i] = pos
                i += 1
        position[i] = n
        ans = 0
        for i in range(k, len(position) - 1):
            totalLeft = position[i - k + 1] - position[i - k]
            totalRight = position[i + 1] - position[i]
            ans += totalLeft*totalRight
            
        return ans
