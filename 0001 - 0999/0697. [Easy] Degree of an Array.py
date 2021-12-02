# https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic, start, end = {}, {}, {}
        n = len(nums)
        for i in range(n):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            if nums[i] not in start:
                start[nums[i]] = i
            end[nums[i]] = i
            
        freq = 0
        for num in dic: 
            freq = max(freq, dic[num])
        
        ans = inf
        
        for num in dic: 
            if dic[num] == freq:
                ans = min(ans, end[num] - start[num] + 1)
        
        return ans
        
