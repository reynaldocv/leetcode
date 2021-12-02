# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def rangeStartEnd(start, end):            
            if start != end: 
                return str(start) + "->" + str(end)
            else:
                return str(start)            
            
        n = len(nums)
        if n == 0: return []
        if n == 1: return [str(nums[0])] 
        ans = []
        start = end = nums[0]        
        for i in range(1, n):             
            if nums[i] == nums[i - 1] + 1:
                end = nums[i]
            else:
                ans.append(rangeStartEnd(start, end))
                start = end = nums[i]
        ans.append(rangeStartEnd(start, end))
        return ans
