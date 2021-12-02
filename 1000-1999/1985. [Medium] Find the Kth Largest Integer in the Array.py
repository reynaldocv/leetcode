# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(reverse = True, key = lambda item: int(item))        
        return nums[k - 1]
        
        
        
