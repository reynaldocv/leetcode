# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        
        nums = [(num, i) for (i, num) in enumerate(nums)]
        
        if indexDifference == 0: 
            nums.sort()
            
            idx = bisect_left(nums, (nums[0][0] + valueDifference, 0))
            
            if idx == n: 
                return [-1, -1]
            
            else: 
                return [nums[0][1],  nums[idx][1]]
            
        else: 
            arr = []
            
            prev = 0 
            
            for (num, i) in nums[indexDifference - 1: ]:
                #print(num, i, arr)
                idx = bisect_left(arr, (num + valueDifference, 0)) 
                
                if idx < len(arr):
                    return (i, arr[idx][1])
                
                idx = bisect_right(arr, (num - valueDifference, inf)) 
                
                if idx > 0:
                    return (i, arr[idx - 1][1])                
                
                insort(arr, nums[prev])
                prev += 1 
                
            return [-1, -1]
                
                
            
        
