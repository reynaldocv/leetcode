# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums) 
        
        ans = []
        
        for i in range(n//2):
            ans.append(nums[i])
            ans.append(nums[i + n//2])
            
        return ans 
