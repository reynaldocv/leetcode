# https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for num in nums: 
            dic[num] = dic.get(num, 0) + 1           
        ans = 0
        for key in dic:
            if key + 1 in dic:
                ans = max(ans, dic[key] + dic[key + 1])
        return ans
