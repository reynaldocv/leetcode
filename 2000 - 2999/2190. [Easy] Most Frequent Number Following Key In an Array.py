# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        
        counter = defaultdict(lambda: 0)
        
        ans = (0, -1)
        
        for i in range(n - 1):
            if nums[i] == key: 
                counter[nums[i + 1]] += 1 
                
                ans = max(ans, (counter[nums[i + 1]], nums[i + 1]))
                
        return ans[1]
            
        
