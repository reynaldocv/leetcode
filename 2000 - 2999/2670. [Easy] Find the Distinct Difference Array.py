# https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        right = defaultdict(lambda: 0)
        left = defaultdict(lambda: 0)
        
        for num in nums: 
            right[num] += 1 
            
        ans = [0 for _ in range(n)]
        
        for (i, num) in enumerate(nums):
            right[num] -= 1 
            
            if right[num] == 0: 
                right.pop(num)
            
            left[num] += 1 
            
            ans[i] = len(left) - len(right)
            
        return ans 
        
        
