# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        if n % k != 0: 
            return False
        
        nums.sort()
        
        while nums:
            num = nums[0]
            for _ in range(k):
                idx = bisect_left(nums, num)
                if idx != len(nums):
                    if nums[idx] == num: 
                        num += 1
                        nums.pop(idx)
                    else: 
                        return False
                else: 
                    return False
                
        return True
        
