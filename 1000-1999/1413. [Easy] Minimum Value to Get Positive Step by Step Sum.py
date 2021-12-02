# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = aux = nums[0]
        for i in range(1, len(nums)):
            aux += nums[i]
            ans = min(aux, ans)
        return 1 if (ans > 0) else -1*ans + 1
