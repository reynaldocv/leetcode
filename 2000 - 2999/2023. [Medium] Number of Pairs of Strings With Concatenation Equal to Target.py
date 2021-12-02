# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/ 

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        nums.sort(key = lambda item: len(item))
        n = len(nums)
        t = len(target)
        
        ans = 0
        start = defaultdict(lambda: 0)
        end = defaultdict(lambda: 0)
        
        for (i, val) in enumerate(nums):
            if len(val) not in start: 
                start[len(val)] = i
            end[len(val)] = i
            
        for (i, num) in enumerate(nums): 
            k = t - len(num)
            for idx in range(start[k], end[k] + 1):
                if idx != i:
                    if num + nums[idx] == target: 
                        ans += 1
        
        return ans
    
        
            
