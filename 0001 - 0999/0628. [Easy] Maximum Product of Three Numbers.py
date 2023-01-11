# https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort() 
        
        num1 = nums[-1]*nums[-2]*nums[-3]
        
        num2 = nums[0]*nums[1]*nums[-1]
        
        return max(num1, num2)
