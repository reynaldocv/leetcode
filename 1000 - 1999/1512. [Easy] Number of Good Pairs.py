# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        ans = 0
        for i in counter.keys():
            ans += counter[i]*(counter[i] - 1)//2
        return ans
            
        
