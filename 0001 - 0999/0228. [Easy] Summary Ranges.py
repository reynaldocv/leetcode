# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: 
            return []
        
        start = prev = nums[0]        
        ans = []
        
        for num in nums[1: ] + [inf]:
            if prev + 1 == num: 
                prev += 1 
            else: 
                if start == prev: 
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(prev))
                    
                prev = start = num
                
        return ans

