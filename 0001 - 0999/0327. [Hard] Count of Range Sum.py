# https://leetcode.com/problems/count-of-range-sum/

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ans = prefix = 0 
        
        arr = [0]
        for num in nums: 
            prefix += num
            
            start = bisect_left(arr, prefix - upper)
            end = bisect_right(arr, prefix - lower)           
            
            ans += end - start 
            
            insort(arr, prefix)
            
        return ans 

class Solution2:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def helper(arr, value):            
            ans = 0 
            
            tmp = []
            
            for num in arr[:: -1]:
                idx = bisect_left(tmp, num + value)

                ans += len(tmp) - idx

                insort(tmp, num)

            return ans 

        prefix = [0]
        
        for num in nums: 
            prefix.append(prefix[-1] + num)
            
        return helper(prefix, lower) - helper(prefix, upper + 1)
        
