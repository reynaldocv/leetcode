# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        n = len(nums)
        aux = 0
        for i in range(n):
            aux = 2*aux + nums[i]
            ans.append(aux % 5 == 0)
        return ans
