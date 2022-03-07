# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        ans = (0, 0)
        n = len(nums)
        
        counter = defaultdict(lambda: 0)
        
        for i in range(1, n):
            counter[nums[i]] += 1 
            if nums[i - 1] == key:
                ans = max(ans, (counter[nums[i]], nums[i]))
                
        return ans[1]  
