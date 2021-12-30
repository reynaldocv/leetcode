# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        arr = []
        for (i, num) in enumerate(nums):
            arr.append(num)
            prev = num
            for numB in nums[i + 1:]:
                prev += numB
                arr.append(prev)
        
        arr.sort()
        
        return sum(arr[left - 1: right]) % MOD
        
        
