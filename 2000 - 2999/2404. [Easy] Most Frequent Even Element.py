# https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ans = (0, inf)
        counter = defaultdict(lambda: 0)
        
        for num in nums:
            if num % 2 == 0:
                counter[num] += 1
                ans = min(ans, (-counter[num], num))
                
        return ans[1] if ans[1] != inf else -1
        
