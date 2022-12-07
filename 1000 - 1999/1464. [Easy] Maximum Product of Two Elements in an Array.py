# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = [0, 0]
        
        for num in nums: 
            insort(arr, num)
            
            arr = arr[1: ]
            
        return (arr[0] - 1)*(arr[1] - 1)
                
        
        
